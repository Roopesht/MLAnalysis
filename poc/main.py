# -*- coding: utf-8 -*-
import features 
import mlRepo
import logger

#Acquire the data
algos = mlRepo.getAlgos(None) 
for key in algos:
    for feat in features.getFeatureSets(features.getAllFeats()):
        accuracy = algos[key].execute(feat, None, None, None)
        logger.logit (algos[key].getName(), accuracy)
        logger.flush()
        #Store the values against the featurs and algos for comparing it later
