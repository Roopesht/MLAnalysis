# -*- coding: utf-8 -*-

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# -*- coding: utf-8 -*-
def getName():
    return "LinearRegression"

def execute(X_train, Y_train, X_test, Y_test):
    reg = LinearRegression()
    reg.fit(X_train, Y_train)
    pred=reg.predict(X_test)
    accuracy = mean_squared_error(Y_test, pred, multioutput='raw_values')
    return accuracy
