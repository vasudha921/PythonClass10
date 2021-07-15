import pandas 
import csv
import numpy as np
import plotly.express as px

 #fig = px.scatter(df, x = 'Size of TV', y = '	Average time spent watching TV in a week (hours)')
 #fig.show()

def getSource(data_path):
    MarksInPercentage = []
    DaysPresent = []
    with open ('Marks vs Dayspresent.csv') as f:
        csvReader = csv.DictReader(f)
        for i in csvReader: 
            MarksInPercentage.append(float(i['Marks In Percentage']))
            DaysPresent.append(float(i['Days Present']))
    return{'x': MarksInPercentage, 'y': DaysPresent}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print(correlation[0,1])

def setup():
    data_path = "Marks vs Dayspresent.csv"
    data_source= getSource(data_path)
    findCorrelation(data_source)

setup()