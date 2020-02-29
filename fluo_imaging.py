import numpy as np 
import matplotlib.pyplot as plt
import os 
import csv
from scipy.optimize import curve_fit

os.chdir('./data/fluorescence/')

#Storing the data, background, and the averaged data

background = []
data1 = []
data2 = [] 
data3 = []
data4 = []
data5 = [] 
time_values = []

averaged_data = []

with open('N1.csv') as file: 
    tempo = csv.reader(file)
    for row in tempo:
        data1.append(row)
file.close()

with open('N2.csv') as file: 
    tempo = csv.reader(file)
    for row in tempo:
        data2.append(row)
file.close()

with open('N3.csv') as file: 
    tempo = csv.reader(file)
    for row in tempo:
        data3.append(row)
file.close()

with open('N4.csv') as file: 
    tempo = csv.reader(file)
    for row in tempo:
        data4.append(row)
file.close()


with open('N_back.csv') as file: 
    tempo = csv.reader(file)
    for row in tempo:
        background.append(row)
file.close()

print(background)
print(data1)
print(data2)
print(data3)
print(data4)
  

print(len(data1))
print(len(data2))
print(len(data3))
print(len(data4))


#Subtract background from data and average data 

for jj in range(len(data1)):
    data1[jj][1] = data1[jj][1] - background[jj][1]
    data2[jj][1] = data2[jj][1] - background[jj][1]
    data3[jj][1] = data3[jj][1] - background[jj][1]
    data4[jj][1] = data4[jj][1] - background[jj][1]

for jj in range(len(data1)):
    averaged_value_jj = (data1[jj][1] + data2[jj][1] + data3[jj][1] + data4[jj][1])/5
    averaged_data.append(averaged_value_jj)
    time_values.append(data1[jj][0])

#Calculate statistics

std_dev = [np.std([data1[jj][1],data2[jj][1],data3[jj][1],data4[jj][1]]) for jj in range(len(data1))]


#Curve fitting the MOT loading curve and determining the laser-cooling rate

x_to_fit = []
y_to_fit = []

def charging_curve(t, alpha, k):
    return(k*(1 - np.exp(-t/alpha)))

p_init = [1,1]
popt, pcov = curve_fit(charging_curve, time_values, p0 = p_init)
fit_data = list(charging_curve(t, *popt), time_values)
uncert = np.sqrt(np.diag(pcov))

alpha = popt[0]
alpha_uncert = uncert[0]
print('$\alpha$ = ' + str(alpha) + str(alpha_uncert))
#Calculate goodness of fit

residuals = [((averaged_data[jj]-fit_data[jj])/std_dev[jj])**2 for jj in range(len(data1))]
chi_square = sum(residuals)/len(residuals)

print('Chi-square for the fit is ' + str(round(chi_square,2)))
fig2 = plt.figure() 
axs2 = fig2.add_subplot(111)
axs2.plot(time_values, fit_data)
axs2.errorbar(x = time_values, y = averaged_data, yerr = std_dev)
plt.plot()

