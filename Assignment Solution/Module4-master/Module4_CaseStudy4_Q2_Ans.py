#Plot Total Sales Per Month for Year 2011 as Bar Chart.  Is Bar Chart Better to visualize than Simple Plot?
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("c:\\temp\\BigMartSalesData.csv")
selected_data=dataset.loc[:,['Month','Quantity']]
x=np.array(selected_data["Month"])
y=np.array(selected_data["Quantity"])
x2=np.unique(x)
y2=selected_data.groupby('Month')['Quantity'].count()
df=pd.DataFrame(y2)
y3=df['Quantity'].values.tolist()
# print y3
plt.bar(x2,y3)
plt.xlabel('Month of Sales')
plt.ylabel('Total Quantity Sales')
plt.grid()
plt.savefig('C:\\Users\\Diwakar\\Pictures\\BarChart001.png')
plt.show()

# Bar Chart isn't the better choice to visualize than Simple Plot
