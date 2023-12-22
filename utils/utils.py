import pickle
import math
import pandas as pd
import numpy as np


# Function to read and rearrange the pickle file
def read_pickle(headers):

    df=pd.DataFrame(columns=headers)

    with (open('./sentiments.pickle', "rb")) as openfile:
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


# Function to log-normalize
def normalize(distributions):
    
    neg=np.array(distributions.iloc[0])
    neg_log=np.zeros_like(neg)
    neut=np.array(distributions.iloc[1])
    neut_log=np.zeros_like(neut)
    pos=np.array(distributions.iloc[2])
    pos_log=np.zeros_like(pos)

    lin=[neg,neut,pos]
    log=[neg_log,neut_log,pos_log]

    for j in range(3):

        for i in range(len(lin[j])):
            if lin[j][i]==0:
                log[j][i]=-1
            else:
                log[j][i]=np.log(lin[j][i])


    minimum=min(np.mean(log[0]),np.mean(log[1]),np.mean(log[2]))

    scalor1=np.mean(log[0])/minimum
    neg_normalized=list(log[0]/scalor1)

    scalor2=np.mean(log[1])/minimum
    neut_normalized=list(log[1]/scalor2)

    scalor3=np.mean(log[2])/minimum
    pos_normalized=list(log[2]/scalor3)

    normalizeds=[neg_normalized,neut_normalized,pos_normalized]

    for normalized in normalizeds:
        for i in range(len(normalized)):
            if normalized[i]<0:
                normalized[i]=0
            else:
                normalized[i]=math.exp(normalized[i])
            
    return normalizeds