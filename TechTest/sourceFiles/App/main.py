from sourceFiles.Services.dailyProcess import country_top50,user_top50
from sourceFiles.Services.weekTop50 import ParseWeekly

country_top50(ParseWeekly())

user_top50(ParseWeekly())

print("daily process has ended")