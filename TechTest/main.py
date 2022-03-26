import pandas as pd
import numpy as np
from Functs import ParseFile_toDf,country_top50,user_top50
from collections import Counter
from guppy import hpy

filename = "sample_listen-2021-12-01_2Mlines.log"

df = ParseFile_toDf(filename)

country_top50(df)

user_top50(df)

h=hpy()
h.heap()
