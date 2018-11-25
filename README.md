# Title
#### "Mitigating the hazards of food allergy"
# Abstract

For the sake of social goodness through data stories, we consider that food dataset has a lot of stories to tell about the patterns of food production, consumption and its positive and negative effects on the world. Hence we will start with the Open Food Facts dataset and use other sources regarding the progress of our ideas.

Our final idea is  "Food allergy", which happens when a human body overreact to exposure to particular substances in the food.
The aim in this idea is to identify the possible allergies that a given unlabeled food may cause and recommend the food that has specific nutrients and doesn't contain given allergens.
Additionally, the recommendation system will be based on the risk additive level. It is known that additives containing nitrites are carcinogens. Still, many food manufacturers produce food with nitrites additives: i.e (14506 products found containing Sodium nitrite which has the moderate risk of cancer cause (found in the Open Food Facts website).
The social goodness will be to help food-allergic people find their health and enough proportion of food easily.

# Research questions

Food Allergy:

1. Food products with no labels about allergies,
2. Food allergy impacts of quality of life,
3. Having a happy life together with food allergy,    
4. Recommending food items with enough nutrients and without allergens through clustering allergic food,
4. Accumulating enough nutrients together with food allergy,  
5. Avoiding allergens requires careful reading of labels and stringent cleaning procedures,
7. Food allergy prevention. 


# Dataset
Open food facts ( https://www.kaggle.com/openfoodfacts/world-food-facts/home) is a free, open, collaborative database of food products from around the world, with ingredients, allergens, nutrition facts and all the tidbits of information we can find on product labels. 

1. The original data has 665.697 observations  with 174 features,
2. We are interested in the products where the allergens and ingredients are present, remaining with  63.732 observations( almost 10% of overall dataset, but enough to make insights),
3. Text fields have different languages ( i.e product_name, allergens, additives,  ingredients_text, so on ).



# Script for milestone 2
1. Explanation why we gave up from Carbon Footprint idea,
2. Feature exploration of nutrients of the products,
3. Transformation of "ingredients_text" and "allergens"  text features into common language.(TBA)



# The list of internal milestones up until project milestone 3 Dec. 16, 2018
Our planned schedule of work till the milestone 3:
1. Week 1:  Finalize the dataset with structured and well-defined features, build a classification model on the data to classify the possible allergic effect of new food from testing dataset. Measure the accuracy of the model. 
2. Week 2:  Build an optimal system of querying to return the best food with a specific amount of nutrition and allergy limitations.
3. Week 3:  Prepare the report on how our model can identify the allergic effect of the food and what recommendations do we have for people with food allergies.
