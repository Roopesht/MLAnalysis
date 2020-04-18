# -*- coding: utf-8 -*-
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
def getName():
    return "RandomForest"

def execute(X_train, y_train, X_test, Y_test):
    clf = RandomForestClassifier(n_jobs=7, random_state=0)
    clf.fit(X_train, y_train)
    pred= clf.predict(X_test)
    accuracy = accuracy_score(Y_test, pred, normalize=True)*100.0
    return accuracy
