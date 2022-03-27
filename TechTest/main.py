import pandas as pd
import numpy as np
from dailyProcess import country_top50,user_top50
from weekTop50 import ParseWeekly
from collections import Counter

df = ParseWeekly()



country_top50(df)

user_top50(df)


