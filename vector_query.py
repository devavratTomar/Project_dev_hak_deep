import pandas as pd
import numpy as np
import pickle as pk
import logging

def load_dataframe(path, sample=None):
    df = pd.read_csv(path, low_memory=False, index_col='code')
    if sample:
        return df.sample(sample)

def save_nutrition_vq_object(obj, file_path='./nutrition_vq.pickle'):
    with open(file_path, 'wb') as handle:
        pk.dump(obj, handle, protocol=pk.HIGHEST_PROTOCOL)

def restore_nutrition_vq_object(file_path='./nutrition_vq.pickle'):
    with open(file_path, 'rb') as handle:
        return pk.load(handle)

class Node:
    """
    Node class for representing node in Binary Search Tree.
    """
    def __init__(self, value=None, right_child=None, left_child=None, parent=None, items=None):
        # Value of the node for comparing with incoming nutrient feature
        self.value = value
        
        # Two children of the current node. If incoming nutrient feature is near left-child's value, we take left route,
        # else take right route.
        # For leaf node children is None
        self.right_child = right_child
        self.left_child = left_child
        
        # Parent node of the current node. Root node's parent is None
        self.parent = parent
        
        # For leaf nodes, the code of food items contained in the current node. For non leaf nodes, this is non.
        self.items = items
        
    def is_root(self):
        return self.parent == None
    
    def is_leaf(self):
        return self.items != None
    
    def has_children(self):
        return self.right_child != None
    

class VectorQuantizationBST:
    """
    class that performs efficient vector quantization and create binary search tree datastructure for searching vectors.
    """

    def __init__(self, data, max_bin_length):
        """
        :param data: A pandas data frame with unique index
        :param max_bin_length: Maximum bin size of cluster
        """
        #TODO: make this as reference
        self.data = data.copy()
        self.__clean_data()
        
        self.max_bin_length = max_bin_length
        
        self.nrows, self.ncols = self.data.shape
        
        # update the initial cluster        
        self.__cluster_root = Node(value=self.data.mean(), items=self.data.index)
    
    def __clean_data(self):
        """
        Since the nutrition facts have different scale for each column, we normalize it.
        We also remove energy_100g feature from the data as energy can be well approximated by other
        nutrition columns.
        """
        logging.info("Cleaning and Normalising the data set")
        
        # self.data.drop('energy_100g', axis=1, inplace=True)
        
        #Remove data samples that have all columns 0.
        self.data = self.data[self.data.sum(axis=1) != 0]
        self.data_orig_mean = self.data.replace(0, np.NaN).mean()
        
        self.data = self.data/self.data_orig_mean
        
        # It may happen that a particular column has all zeros (while testing for 1000 items.)
        self.data.fillna(0., inplace=True)
        self.data = self.data + 1e-8*np.random.rand(self.data.shape[0], self.data.shape[1])
        
        # normalize the vectors to have unit norm as we are computing cosine distance
        self.data = self.data.divide(np.sqrt(np.square(self.data).sum(axis=1)), axis=0)
        
        logging.info("[done] Cleaning and Normalising the data set")
        
    def __2mean_clustring(self, mean1, mean2, cluster_indices):
        data = self.data.loc[cluster_indices]
        is_near_mean1 = data.dot(mean1) > data.dot(mean2)
        
        return data[is_near_mean1].index, data[~is_near_mean1].index
        
    def __split_cluster(self, cluster_mean, cluster_indices):
        mean_1 = cluster_mean + 1e-6*np.random.rand(self.ncols)
        mean_1 = mean_1/(np.sqrt(np.sum(mean_1**2)))
        
        mean_2 = cluster_mean + 1e-6*np.random.rand(self.ncols)
        mean_2 = mean_2/(np.sqrt(np.sum(mean_2**2)))
        cluster_1, cluster_2 = self.__2mean_clustring(mean_1, mean_2, cluster_indices)
        
        cluster_1_mean = self.data.loc[cluster_1].mean()
        cluster_1_mean = cluster_1_mean/np.sqrt(np.sum(cluster_1_mean**2))
        
        cluster_2_mean = self.data.loc[cluster_2].mean()
        cluster_2_mean = cluster_2_mean/np.sqrt(np.sum(cluster_2_mean**2))
        
        return cluster_1_mean, cluster_1, cluster_2_mean, cluster_2
        
    
    def run_next(self):
        logging.info("Splitting current clusters into 2")
        # Either a node has both children or no child at all! So it makes sense to traverse the tree breadth-wise
        queue = []
        queue.insert(0, self.__cluster_root)
        
        # flag to check the tree is full (max_bin_length achieved for all leaves) and letting the caller know.
        is_saturated = True
        while(len(queue)):
            current_node = queue.pop()
            
            if current_node.has_children():
                queue.insert(0, current_node.left_child)
                queue.insert(0, current_node.right_child)
                continue
            
            # Current_node does not have children. So let it make children if she is fertile using its items.
            if len(current_node.items) > self.max_bin_length:
                c1_m, c1, c2_m, c2 = self.__split_cluster(current_node.value, current_node.items)
                # if not able to split current node then don't add childrens
                if len(c1) != 0 and len(c2) != 0:
                    is_saturated = False
                    current_node.left_child  = Node(value=c1_m, parent=current_node, items=c1)
                    current_node.right_child = Node(value=c2_m, parent=current_node, items=c2)

                    # Deleting items of current_node as they are not needed anymore.
                    current_node.items = None
        
        return is_saturated    
    
    def run_all(self):
        while(True):
            if self.run_next():
                break
        print("Binary search tree created!")
    
    def get_similar_food(self, nutrition_feature_100g):
        """
        Make sure nutrition_feature_100g is the original feature without data preprocessing and without energy_100g. Keep the column
        sequence same.
        """
        norm_feature = nutrition_feature_100g/self.data_orig_mean
        norm_feature = norm_feature/np.sqrt(np.square(norm_feature).sum())
        
        current_node = self.__cluster_root
        
        while(current_node.has_children()):
            if np.dot(norm_feature, current_node.left_child.value) > np.dot(norm_feature, current_node.right_child.value):
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
        
        return current_node.items
        
    #TODO:Remove once tested. Just for testing purposes
    def get_all_leaves(self):
        
        queue = []
        queue.insert(0, self.__cluster_root)
        clusters = []
        
        while(len(queue)):
            current_node = queue.pop()
            
            if current_node.has_children():
                queue.insert(0, current_node.left_child)
                queue.insert(0, current_node.right_child)
                continue
            
            clusters.append({'mean': current_node.value, 'indices':current_node.items})
        
        return clusters
        