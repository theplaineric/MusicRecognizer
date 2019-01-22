# coding: utf-8
import pandas as pd
from pydub import AudioSegment
from glob import iglob
import os
# os.path.isfile('')

data = pd.read_csv("C:/Users/theplaineric/Desktop/MusicRecognizer/LibraryList.csv")

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

mp3_files = df[df['ext'] == 'mp3']['path'].tolist()

def convert_mp3_to_wav():
    for file in mp3_files:
        if (not os.path.isfile(file)):
            continue
        mp3_to_wav = AudioSegment.from_mp3(file)
        mp3_to_wav.export(get_file_name(file), format='wav')

def get_file_name(str):
    strList = str.split("/")
    folder_destination = "C:/Users/theplaineric/Desktop/MusicRecognizer/Music Samples/"
    return folder_destination+strList[-1][:-4]+'.wav'

convert_mp3_to_wav()

"""
def delete_wav_files():
    for file in mp3_files:
        if (not os.path.isfile(file)):
            continue
        delete_wav_file = file[:-4]+'wav'
        os.remove(delete_wav_file)

delete_wav_files()
"""
