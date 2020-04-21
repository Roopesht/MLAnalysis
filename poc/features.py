# -*- coding: utf-8 -*-

def getAllFeats():
    pass

def getFeatureSets(df, columns, results):
    mandatory = ['fifth]
    onehastobepresent = [['first'], ['second', 'third'], ['second', 'fourth']]
    segment=[["trend"], ['political', 'recession']]
    minimmum= 4
    maximum=10
    #Shuffle
    feats=[ \
           df[columns[0:3]] , \
           df[columns[1:4]] , \
           df[columns[2:5]] , \
           df[columns[3:6]] , \
           ]
    
           
    return feats
