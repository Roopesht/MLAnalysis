# -*- coding: utf-8 -*-
import features 
import mlRepo
import logger
import sourceData
#Acquire the data
from sklearn.model_selection import train_test_split

df, columns, results = sourceData.getData()
algos = mlRepo.getAlgos(None) 
result=df["result1"]

for feat in features.getFeatureSets(df, columns, results):
    X_train, X_test, Y_train, Y_test = train_test_split(feat, result, test_size=0.4, random_state=101)
    #print ("Count: ", X_train.count(), Y_train.count())
    for key in algos:
        accuracy = algos[key].execute(X_train, Y_train, X_test, Y_test)
        logger.logit (algos[key].getName(), accuracy)
        logger.flush()
        #Store the values against the featurs and algos for comparing it later
