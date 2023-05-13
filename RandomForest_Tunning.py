from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV, train_test_split
from utils import *

# Load the iris dataset and scale the features
y, X = tunning_classifier(directory='./Dataset/')

# Create a Random Forest model
rf = RandomForestClassifier(random_state=0)

# Define the hyperparameter grid to search over
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 5, 10],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['sqrt', 'log2', None],
    'bootstrap': [True, False]
}

# Create a grid search object
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5)

# Fit the grid search object to the training data
grid_search.fit(X, y)

# Print the best parameters found by the grid search
print('Best parameters:', grid_search.best_params_)
