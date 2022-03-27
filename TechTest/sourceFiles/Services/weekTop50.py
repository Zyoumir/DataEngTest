import pandas as pd
import numpy as np
import os
import datetime as dt
from datetime import datetime, timedelta
from tkinter import Tk,filedialog

def getCountryFiles():
    FileNames=[]
    #demanding entry for folder path
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    path = filedialog.askdirectory()
    for file in os.listdir(path):
    # Check whether file is in wanted format or not
        if file.endswith(".log") & file.startswith("listen-"):
            file_path = f"{file}"
            FileNames.append(file_path)
    return FileNames


def getFileDates():
    list= []
    files = getCountryFiles()
    for file in files:
        file = file[7:17:1]
        list.append(dt.datetime.strptime(file,"%Y-%m-%d").date())
    return list
        
def getWeeklyFileNames():
    list= getFileDates()
    weekElements=[]
    for element in list:
        if (element) > (datetime.today().date() - timedelta(days=7)):
            weekElements.append("listen-"+dt.datetime.strftime(element, "%Y-%m-%d")+".log")
    
    return weekElements


# I tested with the .log file, and this implementation will work with the .txt file you receive on a daily basis
def ParseFile_toDf(filename):
    file = open(filename,"r")
    song_id=[]
    user_id=[]
    country=[]
    for line in file.readlines():
        if len(line.split('|')) == 3 :
            song_id.append(line.split('|')[0])
            user_id.append(line.split('|')[1])
            country.append(line.split('|')[2].replace("\n",""))

    data = pd.DataFrame()
    data["song_id"] = song_id
    data["user_id"] = user_id
    data["country"]  = country
    data["country"] = data["country"].apply(lambda x: x[:2] if len(x)>2 else x)
    data["song_id"] = data["song_id"].apply(lambda x: np.nan if ((x == '')|(x=='null')) else x).astype("int32")
    data["user_id"] = data["user_id"].apply(lambda x: np.nan if ((x == '')|(x=='null')) else x).astype("float32")
    del song_id 
    del user_id 
    del country
    del file
    return data

def ParseWeekly():
    #df concat direct
    df = pd.DataFrame()
    listOfWeekFiles= getWeeklyFileNames()
    for i in range(len(listOfWeekFiles)):
        df = pd.concat([df,ParseFile_toDf(listOfWeekFiles[i])])
    del listOfWeekFiles
    return df