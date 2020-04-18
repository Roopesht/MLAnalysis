# -*- coding: utf-8 -*-
import features 
import mlRepo
algos = mlRepo.getAlgos(None)
for key in algos:
    for feat in features.getFeatureSets(features.getAllFeats()):
        accuracy = algos[key].execute(feat, None, None, None)
        print (algos[key].getName(), accuracy)
        #Store the values against the featurs and algos for comparing it later
