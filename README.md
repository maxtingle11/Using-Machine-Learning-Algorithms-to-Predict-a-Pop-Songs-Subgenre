# Predicting Pop Subgenres with Machine Learning Algorithms

Data Scientists - Anastasia Kharina & Max Tingle 

Flatiron School - Machine Learning Project

## Research Question

**Can we predict a pop song's subgenre using its audio features?**

## Dataset

Collected from Spotify's API, our dataset contains audio feature information for 13,988 pop songs. 


## Dependent/Target Variable

The 'target' column in the dataset has categorical labels 1-7 that correspond with the following 7 pop-subgenres:
- 1 = dance-pop
- 2 = rap-pop
- 3 = folk-pop
- 4 = electro-pop
- 5 = rock-pop
- 6 = indie-pop
- 7 = EDM-pop

*The target labels are mutually exclusive, meaning that each song only has one subgenre label.*


## Independent Variables

The remaining columns of the dataset are [audio features](https://developer.spotify.com/documentation/web-api/reference/tracks/get-several-audio-features/) or metrics that measure each song's acousticness, danceability, duration, energy, intrumentalness, key, liveness, loudness, major/minor key, speechiness, tempo, time signature, and valence.


## Modeling Algorithms

We fit models for the following machine learning algorithms, and used Grid Search Cross Validation to hypertune the parameters of each model:
- Logistic Regression
- K-Nearest Neighbors
- Decision Tree Classifier
- Random Forrest Classifier
- AdaBoost Classifier
- Gradient Boost Classifier
- eXtreme Gradient Boost Classifier
- Support Vector Machine

*Not included in our technical notebook: we further tuned each model by: 1) limiting features based on feature importance rankings from Decision Tree Classifier, and 2) applying Principal Component Analysis for dimensionality reduction. Neither of these two adjustments yielded better performing models.*

## Finding

**The model fit with eXtreme Gradient Boost Classifier had the highest accuracy rate of approximately 55%.**

Out of 7 subgenres, there is a 14% chance of randomly picking the correct subgenre. The model fit with XGBoost Classifier is almost 4 times more likely than random chance to correctly classify the pop song to its correct subgenre. 

Our analysis concludes that one can develop a model that predicts a pop song's subgenre with 55% accuracy.


## Future Work

1. In the future, we would like to develop a model that includes more of the 322 pop subgenres that Spotify labels rather than the 7 we limited this project to. 
2. Additionally, we would like to explore models for other major genre groups (eg. Rock, Hip Hop, Country, etc.).


## Repository Files

1. README.md
2. Predicting Pop Subgenres Presentation (PDF)
3. Technical Notebook (Jupyter Notebook)
4. scripts.py (Pre-defined Python functions used in technical notebook)
5. data (Folder containing csv files)
6. images (Folder containing png files exported from technical notebook)


## Responsibilities

- Data Collection & Cleaning - Karin & Max
- Machine Learning Modeling & Feature Engineering - Karin & Max
- Technical Notebook - Karin & Max
- Presentation - Karin & Max
