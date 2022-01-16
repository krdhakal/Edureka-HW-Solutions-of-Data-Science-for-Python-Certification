import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model

dataset=pd.read_csv(r'C:\\Temp\\voice.csv')
df=pd.DataFrame(dataset)
label=dataset.loc[:,['label']]
y=label['label'].tolist()

temp_x=df.iloc[:,0:19].sum(axis=1)
arr_x=np.array(temp_x)
x=list(arr_x)
raw_data={'x':x,'y':y}
df_new=pd.DataFrame(raw_data)
X_train, X_test, y_train, y_test = train_test_split(df_new, y, test_size=0.2)
# fit a model
lm = linear_model.LinearRegression()
model = lm.fit(X_train, y_train)
predictions = lm.predict(X_test)
plt.scatter(y_test, predictions)
plt.xlabel('True Values')
plt.ylabel('Predictions')
plt.show()

