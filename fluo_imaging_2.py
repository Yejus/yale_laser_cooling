import numpy as np 
import matplotlib.pyplot as plt
import os 
import pandas as pd 
from scipy.optimize import curve_fit

background = 0.5343791

df1 = pd.read_csv(r'.\data\fluorescence\N1.csv')
print