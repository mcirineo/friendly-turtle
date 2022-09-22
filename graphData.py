from turtle import up
import pandas as pd   
import numpy as np 
import matplotlib.pyplot as plt 
#Read the text file to put into Pandas Data Table 
df = pd.read_csv("uphRecs.txt", sep = " ") 
print(df) 

#visually represent data 

dates = [] 
upVal = [] 

f = open ('uphRecs.txt', 'r') 
for row in f: 
    row = row.split(' ')
    dates.append(row[0]) 
    upVal.append(row[1]) 
plt.rcParams["figure.figsize"] = [9.50, 10.50]
plt.rcParams["figure.autolayout"] = True
plt.plot(dates, upVal, color = 'b', label = 'UPH Record since 5/22/22')
plt.yticks(np.arange(min(upVal), max(upVal)+1, 1.0))
plt.xlabel('Dates', fontsize = 12) 
plt.ylabel('UPH', fontsize =12 )  

plt.ylim(0,120)

plt.title("UPH Records") 
plt.legend() 
plt.show()


