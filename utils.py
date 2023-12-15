import pickle
import pandas as pd
import numpy as np


def read_pickle(headers):

    df=pd.DataFrame(columns=headers)

    with (open('./tmp/sentiments.pickle', "rb")) as openfile:
        list1=list(pickle.load(openfile).items())
    
    for t in list1:
        name=t[0][:-4]
        pos=t[1][0]
        neutral=t[1][1]
        neg=t[1][2]
        df.loc[len(df)]=[name,pos,neutral,neg]

    return df


# Function to preprocess the text
def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)