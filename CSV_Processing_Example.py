import numpy as np
import pandas as pd #only necessary one
# import matplotlib.pyplot as plt
# import math
# from tkinter.filedialog import askdirectory
# import matplotlib
# from scipy import optimize

from pandas_profiling import ProfileReport

path = 'Dataset'
year = '2019'

# Converting into Dataframe
for i in range(1997,2020):
    for j in range (1, 7):
        df = pd.read_csv('Dataset/' + str(i) +'/Form' + str(j)+ '.csv',encoding='ISO-8859-1')
        # df.head()
        prof=ProfileReport(df)
        prof.to_file("report.html")
        
        




