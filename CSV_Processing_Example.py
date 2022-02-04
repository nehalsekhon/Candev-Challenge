import numpy as np
import pandas as pd #only necessary one
import matplotlib.pyplot as plt
import math
from tkinter.filedialog import askdirectory
import matplotlib
from scipy import optimize

path = 'Dataset'

# Converting into Dataframe
df = pd.read_csv(path+'\Form1.csv')
