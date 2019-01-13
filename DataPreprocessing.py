# coding: utf-8
import pandas as pd
data = pd.read_csv("LibraryList.csv")

def locationProcessing(str):
    sample = "file://localhost/"
    space = "%20"
    str = str.replace(space, " ")
    return str.replace(sample, "")

data['path'] = data['Location'].apply(locationProcessing)
data = data.drop(['Column1', 'Column2', 'Column3','Genre','Play Count'], axis=1)

def isWav(str):
    return str[-3:]
    
data['ext'] = data['path'].apply(isWav)
data['ext'].value_counts()
df = data[(data.ext == 'mp3') | (data.ext == 'wav')]
