# Plotting Graph
# Make a bar plot with each state name on the x -axis and their total benefitted inmates as their bar heights
# Which state has the maximum number of beneficiaries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv('c:\\temp\\prisoners.csv')
df=pd.DataFrame(dataset)
x=df.loc[:,['STATE/UT']]
y=df.iloc[:,2:6].sum(axis=1)
x2=np.array(x)
y2=np.array(y)
x3=list(x2)
y3=list(y2)
plt.plot(x3,y3)
plt.grid()
plt.show()






