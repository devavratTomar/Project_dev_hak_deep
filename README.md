# Title
 "Food allergy" 
# Abstract

For the sake of social goodness through data stories, we consider that food dataset has a lot of stories to tell about the patterns of food production, consumption and its positive and negative effects on the world. Hence we will start with the Open Food Facts dataset and use other sources regarding to the progress of our ideas.

Our final idea is  "Food allergy", which happens when human body overreact to exposure to particular substances in the food.
The aim in this idea is to identify the possible allergies that a given unlabeled food may cause and recommend the food that has specific nutritents and doesn't contain given allergens.
Additionally the recommendation system will be based on the risk additive level. It is known that additives containing nitrites are carcenogenic. Still many food manufacturers produces foodswith nitrites additives: i.e (14506 products found  containing Sodium nitrite which has moderate risk of cancer cause (found in Open Food Facts website).
The social goodness will be to help food allergic people find their healthy and enough proportion of  food easily.

# Research questions

Food Allergy:

1. Grouping ingredients together under the same context using Word2Vec, for e.g. `milk` and `milk solid` should come under `same ingredient context`.
2. Predicting allergens for a food item based on ingredients and additives (optional).
3. Recommending food items based on additives' risk on health.
4. Recommending food items with enough nutrients and without allergens through clustering allergic food.
5. Doing a thorough analysis on allergens/additives present in various food brands/ manufacturing country.




# Dataset
Open food facts ( https://www.kaggle.com/openfoodfacts/world-food-facts/home) is a free, open, collaborative database of food products from around the world, with ingredients, allergens, nutrition facts and all the tidbits of information we can find on product labels. 

1. For our needs, we filtered from the dataset to get the observations which have information about allergens. In the result we have 69101 samples from the whole dataset.
We have observed that  the dataset has language incosistencies in some text features, especially for product_name, ingredients, aditives and allergens. 

# Script for milestone 2
1. Explanation why we gave up from Carbon Footprint idea,
2. Feature exploration and processing of Open Food Facts for Food Allergens
    1. The top 20 additives introduced in the allergens dataset out of 530 additives,
    2. Analyses of nutritional facts of available products and have found some outliers having knowledge that the bound of energy per 100g should be 3700 kJ.
    3.
    4.
    
# A list of internal milestones up until project milestone 3 Dec. 16, 2018
Our planned schedule of work till the milestone 3:
1. Week 1:  Get 
2. Week 2: Work,
3. Week 3:    
