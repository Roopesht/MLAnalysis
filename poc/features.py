# -*- coding: utf-8 -*-

def getAllFeats():
    featuresAll = [[1,2,3,4], [1,2,3,4], [1,2,3,4], [1,2,3,4], [1,2,3,4]] #all feats
    predAll  = [1,2,3,4] # all predictions
    return featuresAll

def getFeatureSets(df, columns, results):
    #Shuffle
    feats=[ \
           df[columns[0:3]] , \
           df[columns[1:4]] , \
           df[columns[2:5]] , \
           df[columns[3:6]] , \
           ]
    
           
    return feats
