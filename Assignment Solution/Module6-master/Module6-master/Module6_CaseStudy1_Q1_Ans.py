# Prisoners dataset sourced from data.gov.in
import pandas as pd
dataset=pd.read_csv(r'c:\\temp\\prisoners.csv')
df=pd.DataFrame(dataset)

# a. Display the first and last five rows in the dataset.
print df.head(5)
print df.tail(5)

# b.Use describe method in pandas and find out the number of columns. Can you say something about those rows who have zero inmates
print 'No. of columns in df DataFrame are ', len(df.columns)
print 'No. of zero inmates'
print df.loc[df['No. of Inmates benefitted by Elementary Education']==0]
df.loc[df['No. of Inmates benefitted by Adult Education']==0]
df.loc[df['No. of Inmates benefitted by Higher Education']==0]
df.loc[df['No. of Inmates benefitted by Computer Course']==0]
