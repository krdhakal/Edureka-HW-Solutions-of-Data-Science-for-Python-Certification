# Module6 Ans 2
import pandas as pd
dataset=pd.read_csv(r'c:\\temp\\prisoners.csv')
df=pd.DataFrame(dataset)

# a.Create a new column total_benefitted that is a sum of inmates benefitted through all modes
print 'total_benefitted=',df.iloc[:,2:6].sum(axis=1)

# b.Create a new row -totals that is the sum of all inmates benefitted through each mode across all states
print df.groupby(['STATE/UT'])[['No. of Inmates benefitted by Elementary Education','No. of Inmates benefitted by Adult Education','No. of Inmates benefitted by Higher Education','No. of Inmates benefitted by Computer Course']].sum()