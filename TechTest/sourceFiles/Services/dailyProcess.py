import pandas as pd
import numpy as np
import json
import time
timestr = time.strftime("%Y%m%d")

def country_top50(df):
    
    GroupDf = df.groupby(['country','song_id']).agg({"user_id":"count"})
    
    my_dict ={}
    for country in GroupDf.reset_index()["country"].unique():
        my_dict[country] = GroupDf.loc[country].sort_values(by="user_id",ascending=False).reset_index().iloc[:50]
    
    
    for key in my_dict.keys():
        with open('./Results/country_top50_'+timestr+'.txt', 'a') as f:
            f.write(key+"|")
            [f.write(str(k)+":"+str(v)+",") for k,v in  my_dict[key].set_index("song_id").to_dict()["user_id"].items()]
            f.write("\n")


def user_top50(df):
    
    GroupDf = df.groupby(['user_id','song_id']).agg({"country":"count"})
    
    my_dict2 ={}
    for user in GroupDf.reset_index()["user_id"].unique():
        my_dict2[user] = GroupDf.loc[user].sort_values(by="country",ascending=False).reset_index().iloc[:50]
    
    for key in my_dict2.keys():
        with open('./Results/user_top50_'+timestr+'.txt', 'a') as f:
            f.write(str(key)[:-2]+"|")
            [f.write(str(k)+":"+str(v)+",") for k,v in my_dict2[key].set_index("song_id").to_dict()["country"].items()]
            f.write("\n")




#4 refacto
#5 crons implementation
#6 result folder
#7 project structuring
#8 readme update