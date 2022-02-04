import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from tkinter.filedialog import askdirectory
import matplotlib
from scipy import optimize

path = askdirectory(title='Select Folder')

# Converting into Dataframe
df = pd.read_csv(path+'\Trial1.csv')
peak_employee_count = df['PEAKEMPLOYEECOUNT'].values
perm_full_time_count = df['PERMFULLTIMECOUNT'].values

# Linear Least Squares Fit
def Delta(x):
  return len(x)*np.sum(x**2)-np.sum(x)**2
def A(x,y):
  return (np.sum(x**2)*np.sum(y)-np.sum(x)*np.sum(x*y))/Delta(x)
def B(x,y):
  return (len(x)*np.sum(x*y)-np.sum(x)*np.sum(y))/Delta(x)
def myquad(x, a,b,c):
  return a*(x-b)**2+c

# plt.errorbar(x=peak_employee_count, y=perm_full_time_count, yerr=y_err, linestyle='None', fmt='x', capsize=2, label='Error')
plt.plot(newx, A(temp, can_pressure_list) + B(temp, can_pressure_list)*newx, color='black', label='Model')
plt.xlabel('Peak Employee Count')
plt.ylabel('Permanent Full Time Count')
plt.legend(loc=0)
plt.savefig(path1 + '\MyFigure.png')
