'''
This class is designed to perform linear regression from scratch

This module implements a simple linear regression model from scratch using gradient descent. 
The LinearRegression class is used to train a model on the relationship for y given a value of x, shown in the equation:
y = mx + c

The model iterates on the gradient(m) and the y-intercept (c) to produce an accurate prediction

Example:
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([2, 4, 6, 8, 10])

    model = LinearRegression(learning_rate=0.01, n_int=1000)
    model.model(X, y)
    predictions = model.predict(X)
'''

# Import required libraries
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn import datasets
from sklearn.model_selection import train_test_split

data = load_diabetes() #detes dataset

X = data.data #patients measurements (height, weight, etc)
y = data.target #disease progression score for diabetes
#made up data

class LinearRegression:

    '''
    Implements a simple linear regression model using gradient descent.
    This class learns the relationship between input features (X) and target values (y) using the linear equation:

    y = mx + c

    '''

    def __init__(self, learning_rate = 0.01, n_int= 1000):  
        self.learning_rate = learning_rate
        self.n_int = n_int
        self.m = None
        self.c = None
#initalize functions, sets the learning rate and how much it should iterate along with establishing self and the objects inside
    def model(self, X, y):
        n_rows, n_columns = X.shape
        self.m = np.zeros(n_columns)
        self.c = 0
#y = mx + c
        for i in range(self.n_int):
            y_predict = np.dot(X, self.m) + self.c
            dm = (1/n_rows) * np.dot(X.T, (y_predict - y))
            dc = (1/n_rows) * np.sum(y_predict-y)

            self.m = self.m - (self.learning_rate * dm)
            self.c = self.c - (self.learning_rate * dc)
   #the model, m is set to a matrix of 0 with n_rows and n_columns
   #iteration occurs to the amount of times established by n_int, in this case 1000
   # change in m and c is calculated using the formula before then being used to update the m and c values when multiplied with 
   # the learning rate
    

    def predict(self, X):
        y_predict = np.dot(X, self.m) + self.c#y = mx + c
        return y_predict
    #returns the matrix multiplication of all the X values along with all the M values and sums them up before adding it with c
    #this is then used to predict values of y when given values of x

X, y=datasets.make_regression(n_samples=100, n_features=1, noise=20, random_state=4)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

model1 = LinearRegression(learning_rate=0.01, n_int=1000)
model1.model(X_train, y_train)

truepredictions = model1.predict(X_test)

print(truepredictions[:10])