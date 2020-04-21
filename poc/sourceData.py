# -*- coding: utf-8 -*-
import pandas as pd

#Add the columns "Long Term Trend", "Short term Trend", "Thursday", "Last 2 hours on thursday", "Tirst 30 minutes of the day"
def getData ():
    df = pd.read_csv ("testdata.csv")
    #db_connection.close()
    columns = ['ID', 'UnderlyingValue', 'PrevId', 'MaxPain', 'PCR', 'maxpain_start', 'underlying_start', 'PCR_start', 'lowerrangevalue', 'upperrangevalue', 'rangespike', 'max', 'min']
    results=[ 'result1', 'result2']
    return df, columns, results
