#Plot Pie Chart for Year 2011 Country Wise. Which Country contributes highest towards sales?
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("c:\\temp\\BigMartSalesData.csv")
selected_data=dataset.loc[:,['Country','Quantity']]
labels_country=np.array(selected_data['Country'])
x_values=np.array(selected_data['Quantity'])
country=np.unique(labels_country)
final_x_values=selected_data.groupby('Country')['Quantity'].count()
# plt.figure(figsize=(40,40))
fig1, ax1 = plt.subplots()
ax1.axis('equal')
plt.pie(final_x_values,labels=country)
plt.savefig('C:\\Users\\Diwakar\\Pictures\\Pie_Chart.png')
plt.show()

