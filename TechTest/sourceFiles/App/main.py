import pandas as pd
import numpy as np
from sourceFiles.Services.dailyProcess import country_top50,user_top50
from sourceFiles.Services.weekTop50 import ParseWeekly
print("test0")
df = ParseWeekly()
print("test1")
country_top50(df)
print("test")

#user_top50(df)


