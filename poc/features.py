# -*- coding: utf-8 -*-

def getAllFeats():
    featuresAll = [[1,2,3,4], [1,2,3,4], [1,2,3,4], [1,2,3,4], [1,2,3,4]] #all feats
    predAll  = [1,2,3,4] # all predictions
    return featuresAll

def getFeatureSets(featAll):
    #Shuffle
    feats=[ \
           [featAll[0], featAll[1], featAll[2] ], \
           [featAll[1], featAll[2], featAll[3] ], \
           [featAll[2], featAll[3], featAll[4] ], \
           [featAll[1], featAll[3], featAll[4] ], \
           [featAll[0], featAll[2], featAll[3] ], \
           [featAll[0], featAll[3], featAll[4] ] \
           ]
           
    return feats
