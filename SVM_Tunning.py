from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from utils import *
# Load the iris dataset and scale the features
print("hello")
y, X = tunning_classifier(directory='./Dataset_new_filtered/')
print("hello2")

# Define the parameter grid
param_grid = {'C': [0.1, 1, 10],
              'kernel': ['rbf', 'poly'],
              'degree': [2, 3, 4],
              'gamma': ['scale', 'auto', 0.1, 1, 10],
              'coef0': [-1, 0, 1]}

# Create an SVM model
svm = SVC()

# Perform a grid search
grid_search = GridSearchCV(svm, param_grid, cv=5)
grid_search.fit(X, y)

# Print the best hyperparameters
print(grid_search.best_params_)