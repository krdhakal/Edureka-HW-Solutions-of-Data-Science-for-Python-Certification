import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

data=pd.read_csv("c:\\temp\\voice.csv")
data.drop("Unnamed: 25",axis=1, inplace=True)
data.columns
data.drop("meanfreq",axis=1, inplace=True)
data['label']=data['label'].map({'M':1,'F':0})
corr=data.corr()
plt.figure(figsize=(14,14))
sns.heatmap(corr,cbar=True,square=True,cmap='label')
plt.show()