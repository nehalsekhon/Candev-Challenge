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
voltage = df['Voltage'].values
current = df['Current'].values

# Linear Least Squares Fit
def Delta(x):
  return len(x)*np.sum(x**2)-np.sum(x)**2
def A(x,y):
  return (np.sum(x**2)*np.sum(y)-np.sum(x)*np.sum(x*y))/Delta(x)
def B(x,y):
  return (len(x)*np.sum(x*y)-np.sum(x)*np.sum(y))/Delta(x)
def myquad(x, a,b,c):
  return a*(x-b)**2+c

plt.errorbar(voltage, current, zorder=1)
plt.plot(xtest, myquad(xtest, popt[0], popt[1], popt[2]), '--r', zorder=2)
plt.xlabel('Voltage (V)')
plt.ylabel('Current (pA)')

plt.savefig(path + '\Fig1.png')
