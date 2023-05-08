from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load the iris dataset
# iris = datasets.load_iris()
# X = iris.data
# y = iris.target
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
def SVM_Model(X_train, X_test, y_train, y_test):
# Split the dataset into training and testing sets

    # Create an SVM model
    svm = SVC(kernel='linear', C=1, random_state=0)

    # Train the SVM model on the training set
    svm.fit(X_train, y_train)

    # Make predictions on the testing set
    y_pred = svm.predict(X_test)


    return svm,y_pred
