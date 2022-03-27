from sourceFiles.Services.dailyProcess import country_top50,user_top50
from sourceFiles.Services.weekTop50 import ParseWeekly

country_top50(ParseWeekly())

print("Top 50 songs in each country done")

user_top50(ParseWeekly())

print("Top 50 songs for each user done")

print("daily process has ended")