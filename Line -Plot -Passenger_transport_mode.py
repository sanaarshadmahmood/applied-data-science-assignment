# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 18:58:34 2023
Passenger transport by mode in United Kingdom.
@author:SANA
ource:https://www.ons.gov.uk/peoplepopulationandcommunity/leisureandtourism/
articles/howwetravel/2015-02-19

"""
#importing python libraries.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#reading data from csv file and assigning it to a dataframe.
df = pd.read_csv('Passenger-transport-by-mode.csv', skiprows= 2)
print(df)
x = np.linspace(1980, 2013, 34)
print(x)

#extracting values from DataFrame created above.
y = np.array(df.iloc[:, 1])#passenger kilometres values for buses and coaches 
w = np.array(df.iloc[:, 2])#passenger kilometres values for cars,vans & taxis.
z = np.array(df.iloc[:, 3])#passenger kilometres values for rail.

#Plotting graph of extracted values.
fig = plt.figure(figsize=(8, 5))
plt.plot(x, y, "r-", label="Buses and Coaches")
plt.plot(x, w, "g-", label="Cars,vans & taxis")
plt.plot(x, z, "b-", label="Rail")

#formatting line graph
plt.xlim(1980, 2013)
plt.title("Passenger transport by mode in Great Britain from 1980 to 2013")
plt.xlabel("Year")
plt.ylabel("(billions passenger kilometres)")
plt.legend(loc="best")
