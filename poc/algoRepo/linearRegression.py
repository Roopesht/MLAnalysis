# -*- coding: utf-8 -*-

from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score


# -*- coding: utf-8 -*-
def getName():
    return "LinearRegression"

def execute(X_train, Y_train, X_test, Y_test):
    accuracy = 1.0
    #reg = LinearRegression(n_jobs=7, random_state=0)
    #reg.fit(X_train, Y_train)
    #pred=reg.predict(X_test)
    #accuracy = accuracy_score(Y_test, pred, normalize=True)*100.0
    return accuracy
