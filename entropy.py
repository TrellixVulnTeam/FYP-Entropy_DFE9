import nltk
import sqlite3
import math
import matplotlib
import numpy as np
import pandas as pd

con = sqlite3.connect('eng.db')

dataframe1 = pd.read_sql_query("""SELECT sid, cid, clemma, tag, tags FROM concept""",con)

#Following function to add average ambiguity (nlogn) and remove any blank tagged entries.
def rowchanger(datalist):
    sid, cid, clemma, tag, tags = datalist
    if not tags == None:
        newtags = tags.replace(";", "").split()
        avgAmbig = 1/len(newtags) * math.log(1/len(newtags))
    else:
        newtags = []
        avgAmbig = None
    return [sid, cid, clemma, tag, newtags, avgAmbig]

dataframe1 = dataframe1.apply(rowchanger, axis = 1, result_type = "expand")
dataframe1.rename(columns={0:"sid", 1:"cid", 2:"clemma", 3:"tag", 4:"newtags", 5:"avgAmbig"}, inplace=True)

#print(dataframe1)

def freqOfOccurrence(datalist):
    occurrenceDictionary = {}
    sid, cid, clemma, tag, newtags, avgAmbig = datalist
    for line in datalist:
        for tag in line:
            if tag not in occurrenceDictionary:
                occurrenceDictionary[tag] = 0
            occurrenceDictionary[tag] += 1
    return occurrenceDictionary
#print(freqOfOccurrence(dataframe1))
#print(dataframe1["tag"].value_counts())
    #THIS ONE IS FOR COUNTING

dataframe1["tag"].value_counts().plot(kind = "bar")

#sum nlogn for entropy

    #check entropy scale limits

    #calculate average ambiguity, even distribution entropy, actual entropy
    #if ignoring 'weird' tags (eg x, w, etc), actual entropy including ALL tags
    #print top 10 bottom 10 for each
    #pick random words to check calculations are correct
    #check which words have most and least difference between pure random vs weighted
    #assume 0 for 0 AND/OR assume + 1/n for 0

    ##consider examining other corpora, differences between genres
