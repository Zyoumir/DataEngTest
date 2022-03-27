from weekTop50 import getWeeklyFileNames
import pandas as pd

def parseWeekToDf():
    weekFiles = getWeeklyFileNames
    
    for file in weekFiles:
        dailyFile = open(file,"r")
    
    song_id ,user_id, country=([], ) * 3
    
    for line in dailyFile.readlines():
        country.append(line.split('|')[0])
        song_id.append(line.split('|').split(':'))

