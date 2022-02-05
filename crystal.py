import numpy as np
import pandas as pd #only necessary one
# import matplotlib.pyplot as plt
# import math
# from tkinter.filedialog import askdirectory
# import matplotlib
# from scipy import optimize

# from pandas_profiling import ProfileReport

path = 'Dataset'
year = '2019'

# Converting into Dataframe
for i in range(1997,2020):
    for j in range (1, 7):
        df = pd.read_csv('Dataset/' + str(year) +'/Form' + str(j)+ '.csv',encoding='ISO-8859-1')
        # grouped_df = df.groupby(['LOCATION']).max()
        # print(grouped_df['NAICSID'])
        id_canada_df=df[df['LOCATION']=='Canada']
        if j==1:
            id_canada_df.to_excel('output1.xlsx')
        elif j==2:
            id_canada_df.to_excel('output2.xlsx')
        elif j==3:
            id_canada_df.to_excel('output3.xlsx')
        elif j==4:
            id_canada_df.to_excel('output4.xlsx')
        elif j==5:
            id_canada_df.to_excel('output5.xlsx')
        elif j==6:
            id_canada_df.to_excel('output6.xlsx')
       

        
        




    