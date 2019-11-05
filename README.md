# Using Machine Learning to Predict a Pop Song's Subgenre

Data Scientists - Anastasia Kharina & Max Tingle 

Flatiron School - Machine Learning Project

## Research Question

Can we predict a pop song's subgenre using its audio features?

## Dataset

The dataset was retrieved from Spotify’s API and contains audio feature information for 13,988 pop songs.

## Dependent/Target Variable

The 'target' column in the dataset has categorical labels 1-7 that correspond with the following 7 pop-subgenres:
- 1 = Dance-Pop
- 2 = Rap-Pop
- 3 = Folk-Pop
- 4 = Electro-Pop
- 5 = Rock-Pop
- 6 = Indie-Pop
- 7 = EDM-Pop

*The target labels are mutually exclusive, meaning that each song only has one subgenre label.*


## Independent Variables

The remaining columns of the dataset are [audio features](https://developer.spotify.com/documentation/web-api/reference/tracks/get-several-audio-features/) or metrics that measure each song's acousticness, danceability, duration, energy, instrumentalness, key, liveness, loudness, major/minor key, speechiness, tempo, time signature, and valence.


## Modeling Algorithms

We fit models for the following machine learning algorithms, and used Grid Search Cross Validation to hyper-tune the parameters of each model:
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

Out of 7 subgenres, there is about a 14% chance of randomly picking the correct subgenre. **The model we fit with the Gradient Boost Classifier had the highest accuracy rate of approximately 56%,** making it 4 times more likely than random chance to correctly classify a pop song to its correct subgenre. 

Our analysis suggests that one can use audio features to predict a pop song's subgenre with 56% accuracy.


## Future Work

1. In the future, we would like to develop a model that includes more of the 322 pop subgenres that Spotify labels rather than the 7 we chose for the scope of this project. 
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
