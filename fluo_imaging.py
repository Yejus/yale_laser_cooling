#Too slow!! and crashes!! 
import numpy as np 
import matplotlib.pyplot as plt
import os 
import csv
from scipy.optimize import curve_fit

os.chdir('./data/fluorescence/')

#Reading data off CSV files into lists (not arrays, because I'm a caveman)

nback = 0.5348
background = 0.5343791
data1 = []
data2 = [] 
data3 = []
data4 = []
time_values = []

averaged_data = []

with open('N1.csv') as file: 
    next(file)
    next(file)
    next(file)
    tempo = csv.reader(file)
    for row in tempo:
        data1.append(row)
file.close()

with open('N2.csv') as file: 
    next(file)
    next(file)
    next(file)
    tempo = csv.reader(file)
    for row in tempo:
        data2.append(row)
file.close()

with open('N3.csv') as file: 
    next(file)
    next(file)
    next(file)
    tempo = csv.reader(file)
    for row in tempo:
        data3.append(row)
file.close()

with open('N4.csv') as file: 
    next(file)
    next(file)
    next(file)
    tempo = csv.reader(file)
    for row in tempo:
        data4.append(row)
file.close()


for jj in range(len(data1)):
    data1[jj][1] = float(data1[jj][1]) - background
for jj in range(len(data2)):
    data2[jj][1] = float(data2[jj][1]) - background
for jj in range(len(data3)):
    data3[jj][1] = float(data3[jj][1]) - background
for jj in range(len(data4)):
    data4[jj][1] = float(data4[jj][1]) - background

data1yval = [data1[jj][1] for jj in range(len(data1))]
data1timeval = [data1[jj][0] for jj in range(len(data1))]

plt.plot(data1timeval, data1yval)
plt.show()