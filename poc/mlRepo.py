# -*- coding: utf-8 -*-
#return the Algos based on the configuration passed
import algoRepo.randomForest as rf
import algoRepo.linearRegression as lr
algoDict = {
    "rf": rf, 
    "lr": lr
        }
def getAlgos(conf):
    return algoDict