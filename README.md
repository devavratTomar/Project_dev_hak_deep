# Title
#### "Mitigating the hazards of food allergy"
# Abstract

For the sake of social goodness through data stories, we consider that food dataset has a lot of stories to tell about the patterns of food production, consumption and its positive and negative effects on the world. Hence we will start with the Open Food Facts dataset and use other sources regarding the progress of our ideas.

Our final idea is  "Food allergy", which happens when a human body overreact to exposure to particular substances in the food.
The aim in this idea is to identify the possible allergies that a given unlabeled food may cause and recommend the food that has specific nutrients and doesn't contain given allergens.
Additionally, the recommendation system will be based on the risk additive level. It is known that additives containing nitrites are carcinogens. Still, many food manufacturers produce food with nitrites additives: i.e (14506 products found containing Sodium nitrite which has the moderate risk of cancer cause (found in the Open Food Facts website).
The social goodness will be to help food-allergic people find their health and enough proportion of food easily.

# Dataset
Open food facts ( https://www.kaggle.com/openfoodfacts/world-food-facts/home) is a free, open, collaborative database of food 
products from around the world, with ingredients, allergens, nutrition facts and all the tidbits of information we can find on product labels. 

1. The original data has 665,697 observations  with 174 features.
2. We are interested in the products where the allergens and categories are present, remaining with  54,896 observations( almost 10% of overall dataset, but enough to make insights).
3. Text fields have different languages ( i.e product_name, allergens, additives, categories so on ). The text fields are present in more than 15 languages.

# Description of important files in the repo

1. `MS3_notebook.ipynb`: The notebook which contains the code for Milestone 2 and 3.
2. `vector_query.py`: The python module which contains the code for Vector Quantisation.
3. `original_allergens.txt`: The original 3000+ unique allergens present in the dataset.
4. `english_allergens.txt`: The translated allergens for the original file present in the dataset.

# Research questions answered

Food Allergy questions answered:

1. Grouping allergens together under the same context using Word2Vec, for e.g. `milk` and `milk solid` should come under `same ingredient context`.
2. Predicted allergens for a food item based on categories.
3. Recommended food items with enough nutrients and without allergens by clustering on all food products for which data was applicable.
4. Did a thorough analysis on allergens/additives present in various food brands, products and manufacturing country.

# Process involved

After working on the dataset analysis and data cleaning parts in Milestone 2; for milestone 3 we used the `nltk` library with a pretrained model (GloVe) to group allergens together under the same context. This was followed by assigning all the products under a group of allergens such as `wheat/flour`, `seafood` etc. Then, to find the products with the same nutritional value but different allergens, we used the technique of Vector Quantisation on Binary Trees. A descriptive analysis of the allergens and additives was performed to answer the following questions: Which product has more allergen? Which brands has more allergens in their product? Also a model was constructed to predict allergens given the categories. For this we used the Random Forest algorithm and achieved testing accuracy of 89.88%. Ingredients were not used to predict allergens since the ingredients data was inconsistent and was in different languages because of which it was hard to translate or train Word2Vec model on it.

# Contribution by group members

- Harshdeep: Word2Vec Feature Engineering and data cleaning for allergens, construction of model using Random Forest for categories and allergens
- Devavrat Tomar: Vector Quantisation and data clearning of nutrients, tabulating final results of the Random forest model
- Mariam Hakobyan: Analysis on allergens/additives present in food products, Data cleaning for categories

The report was written by everyone for each part they did as mentioned above.

For the final presentation, 2 of the group members (Mariam and Devavrat) will work on making of the poster while the other group member (Harshdeep) will present the poster and the project.
