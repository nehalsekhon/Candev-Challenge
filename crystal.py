import numpy as np
import pandas as pd #only necessary one
import matplotlib.pyplot as plt


# import math
# from tkinter.filedialog import askdirectory
# import matplotlib
# from scipy import optimize

# from pandas_profiling import ProfileReport
pd.options.mode.chained_assignment=None

path = 'Dataset'
year = '2019'

# Converting into Dataframe
# for i in range(1997,2020):
# for j in range (1, 7):
#     df = pd.read_csv('Dataset/' + str(year) +'/Form' + str(j)+ '.csv',encoding='ISO-8859-1')
    
#     id_canada_df=df[df['LOCATION']=='Canada']
#     if j==1:
#         id_canada_df.to_excel('output1.xlsx')
#     elif j==2:
#         id_canada_df.to_excel('output2.xlsx')
#     elif j==3:
#         id_canada_df.to_excel('output3.xlsx')
#     elif j==4:
#         id_canada_df.to_excel('output4.xlsx')
#     elif j==5:
#         id_canada_df.to_excel('output5.xlsx')
#     elif j==6:
#         id_canada_df.to_excel('output6.xlsx')

# Canadian Citizen Workforce

dfT=pd.read_csv('Dataset/'+ 'CanadianCitizenWorkforcePopulation.csv')
Pop_Canada=dfT[dfT['Region']=='Canada']
# Pop_Canada_EEOG=Pop_Canada[Pop_Canada['Employment Equity Occupational Groups']]
# print(Pop_Canada.head())
Pop_Canada.to_csv('CCWP.csv')

df_CCWP=pd.read_csv('CCWP.csv')

first_row=df_CCWP.iloc[0]
title_array=[]
percent_array=[]

for col in df_CCWP.columns:
    if ('%' in col and col != '%'):
        title_array.append(col)
        percent_array.append(first_row[col])

title_array.pop(4)
percent_array.pop(4)

print(percent_array)
plt.pie(percent_array, labels = title_array)
plt.savefig("pie.png")






        
        




    