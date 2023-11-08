
"""
Created on Fri Nov  3 01:34:23 2023

@author: SANA
    
source of data: https://www.gov.uk/government/statistics/annual-savings-
statistics
"""
#importing Python libraries.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#reading data from excel file using pandas. header and DataFrame data.
head = pd.read_excel("ISAs.xlsx", sheet_name='ISAs', nrows=6)
df = pd.read_excel("ISAs.xlsx", sheet_name='ISAs',
                   skiprows=6, usecols='B:J', index_col='Area')
print(df)

"""market value ranges (thousands) of individual savings accounts in June 2021 
in United Kingdom."""

x = ["(£1-£2,499)", "(£2,500-£4,999)", "(£5,000-£9,999)", "(£10,000-£14,999)",
     "(£15,000-£19,999)", "(£20,000-£24,999)", "(£25,000-£49,999)",
     "(£50,000&above)"]

#extracting values from DataFrame.

a = list(df.iloc[0, :])
b = list(df.iloc[1, :])
c = list(df.iloc[2, :])
total_no_ISAs = np.array(df.iloc[-1, :])

#Plotting extracted values in a bar graph
fig = plt.figure()
plt.figure(0, figsize=(15, 10))
plt.bar(x, total_no_ISAs)

#formatting bar graph.
plt.title("Individual savings accounts for UK residents in June 2021")
plt.xlabel("market values range (thousands)")
plt.ylabel("number of ISAs")
plt.show()
plt.savefig("Individual_savings.jpg")
