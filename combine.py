from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from utils import *

# # Load and split the data into training and validation sets
Xtrain, Xtest, ytrain, ytest = load_data(directory='./Dataset/')


# Train a Random Forest classifier on the training set
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(Xtrain, ytrain)

# Extract the predicted probabilities of the Random Forest classifier as features
X_train_rf = rf.predict_proba(Xtrain)
X_val_rf = rf.predict_proba(Xtest)

# Concatenate the Random Forest features with the original features
X_train_combined = np.concatenate([Xtrain, X_train_rf], axis=1)
X_val_combined = np.concatenate([Xtest, X_val_rf], axis=1)

# Train an SVM classifier on the combined features
# svm = SVC(kernel='rbf', C=1, gamma='scale', probability=True)
svm = SVC(kernel='poly', C=0.1, random_state=0, coef0=1, degree=4, gamma=0.1, probability=True)
svm.fit(X_train_combined, ytrain)

# Evaluate the performance of the combined classifier on the validation set
y_val_pred = svm.predict(X_val_combined)
accuracy = accuracy_score(ytest, y_val_pred)
print(f"Validation accuracy: {accuracy}")

# Evaluate the performance of the combined classifier on the test set
X_test_rf = rf.predict_proba(Xtest)
X_test_combined = np.concatenate([Xtest, X_test_rf], axis=1)
y_test_pred = svm.predict(X_test_combined)
accuracy = accuracy_score(ytest, y_test_pred)
print(f"Test accuracy: {accuracy}")