# Plot Scatter Plot for the invoice amounts and see the concentration of amount.
# In which range most of the invoice amounts are concentrated
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("c:\\temp\\BigMartSalesData.csv")
selected_data=dataset.loc[:,['Country','Amount']]
x=np.array(selected_data["Country"])
y=np.array(selected_data["Amount"])
x2=np.unique(x)
y2=selected_data.groupby('Country')['Amount'].sum()
df=pd.DataFrame(y2)
y3=df['Amount'].values.tolist()
plt.scatter(x2,y3)
plt.xlabel('Country')
plt.ylabel('Amount')
plt.savefig('c:\\Users\\Diwakar\\Pictures\\scatter_graph001.png')
plt.show()


