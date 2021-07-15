import pandas 
import csv
import numpy as np
import plotly.express as px

 #fig = px.scatter(df, x = 'Size of TV', y = '	Average time spent watching TV in a week (hours)')
 #fig.show()

def getSource(data_path):
    sizeofTV = []
    averageTimeSpent = []
    with open ('TV vs SpentWatching.csv') as f:
        csvReader = csv.DictReader(f)
        for i in csvReader: 
            sizeofTV.append(float(i['Size of TV']))
            averageTimeSpent.append(float(i['	Average time spent watching TV in a week (hours)']))
    return{'x': sizeofTV, 'y': averageTimeSpent}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print(correlation[0,1])

def setup():
    data_path = "TV vs SpentWatching.csv"
    data_source= getSource(data_path)
    findCorrelation(data_source)

setup()