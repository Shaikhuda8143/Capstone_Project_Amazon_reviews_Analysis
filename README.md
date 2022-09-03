# Project_Amazon_reviews_Analysis

## Business Objective:
Need to get the daily analysis of a product listed on **Amazon** such as emotions, sentiments like positive or negative

### Our Product
![echo-dot-3-charcoal-1](https://user-images.githubusercontent.com/97623883/184384384-0040b721-b943-4f7b-aad4-488e869416a4.jpg)

### Approach:
*  Web scraping, collected around 5000 reviews along with ratings, date, title, helpful votes, etc.
* Performed EDA using Plotly, text cleaning, and pre-processing using TextBlob, NLTK, Spacy, and 
CountVectorizer.
*  Models Used Naïve Bayes(51%Accuracy), Logistic Regression(90%Accuracy)
*  Evaluation Ensemble algorithms: AdaBoost, Gradient Boost, Random Forest, Extra trees, etc.
* Evaluation Classification Algorithm: KNN, CART, SGD, SVC, etc.

## Insights:
#### 1)The sales of the device were more in 2019(2019) and gradually decreased in 2020(1528) and number of negative reviews has also increased, So we need to update the product features.

![2022-05-05 (5)](https://user-images.githubusercontent.com/97623883/185196531-2d7e1ce2-464a-45ab-be19-6537aec07c5b.png)

#### 2) We can take the reviews of the customers who gave 5-star rating but having negative and neutral sentiment in their reviews
![Screenshot (60)](https://user-images.githubusercontent.com/97623883/185430914-e3f87c3b-6b2e-4e2f-87d4-7dd5e2003a05.png)
