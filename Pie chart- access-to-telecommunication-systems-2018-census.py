# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 16:54:38 2023

@author: SANA 
source: https://www.stats.govt.nz/information-releases/2018-census-totals-by-topic-national-highlights-updated

"""
#importing python libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#reading data from a CSV file into a DataFrame
dataf = pd.read_csv("access-to-telecommunication-systems-2018-census-csv.csv")
print(dataf)

#extracting values in form of array from a DataFrame.
y = np.array(dataf.iloc[0:6, 2])
print(y)

#creating labels for pie chart plot
mylabels = ["No access to telecommunication systems",
"Access to a cellphone/mobile phone","Access to a telephone",
"Access to the internet","Response unidentifiable","Not stated"]

#plotting a pie chart
plt.pie(y,labels=mylabels)
plt.title("A pie chart of telecom systems access in NZ as per 2018 Census")
