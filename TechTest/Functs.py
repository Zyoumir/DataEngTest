from re import A
import pandas as pd
import numpy as np
import json
import time
timestr = time.strftime("%Y%m%d")

# I tested with the .log file, and this implementation will work with the .txt file you receive on a daily basis
def ParseFile_toDf(filename):
    file = open(filename,"r")
    song_id=[]
    user_id=[]
    country=[]
    a=0
    for line in file.readlines():
        if len(line.split('|')) == 3 :
            song_id.append(line.split('|')[0])
            user_id.append(line.split('|')[1])
            country.append(line.split('|')[2].replace("\n",""))
        


        
    data = pd.DataFrame()
    data["song_id"] = song_id
    data["user_id"] = user_id
    data["country"]  = country
    data ["country"] = data["country"].apply(lambda x: x[:2] if len(x)>2 else x)
    
    return data

def country_top50(df):
    
    GroupDf = df.groupby(['country','song_id']).agg({"user_id":"count"})
    
    my_dict ={}
    for country in GroupDf.reset_index()["country"].unique():
        my_dict[country] = GroupDf.loc[country].sort_values(by="user_id",ascending=False).reset_index().iloc[:50]
    
    
    for key in my_dict.keys():
        with open('country_top50_'+timestr+'.txt', 'a') as f:
            f.write(key+"|")
            [f.write(k+":"+str(v)+",") for k,v in  my_dict[key].set_index("song_id").to_dict()["user_id"].items()]
            f.write("\n")


def user_top50(df):
    
    df["user_id"].replace('null', np.NAN, inplace = True)
    df.replace('', np.NAN, inplace = True)
    df.dropna()
    GroupDf = df.groupby(['user_id','song_id']).agg({"country":"count"})
    
    my_dict2 ={}
    for user in GroupDf.reset_index()["user_id"].unique():
        my_dict2[user] = GroupDf.loc[user].sort_values(by="country",ascending=False).reset_index().iloc[:50]
    
    for key in my_dict2.keys():
        with open('user_top50_'+timestr+'.txt', 'a') as f:
            f.write(key+"|")
            [f.write(k+":"+str(v)+",") for k,v in my_dict2[key].set_index("song_id").to_dict()["country"].items()]
            f.write("\n")
