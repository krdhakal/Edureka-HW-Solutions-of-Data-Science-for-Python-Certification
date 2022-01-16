# Domain –Education
import glob
import csv
import pandas as pd
csvfiles = glob.glob('c:/temp/score/*.csv')
wf = csv.writer(open('c:/temp/score/ScoreFinalTemp.csv','wb'),delimiter = ',')
for files in csvfiles:
    rd = csv.reader(open(files,'r'), delimiter = ',')
    # rd.next() # To skip header
    for row in rd:
        # print row
        wf.writerow(row)

data = pd.read_csv('c:/temp/score/ScoreFinalTemp.csv')
data = data.drop(['Name','Ethinicity'],axis=1)
data.to_csv('c:/temp/score/ScoreFinal.csv')

rd = csv.reader(open('c:/temp/score/ScoreFinal.csv','r'), delimiter = ',')
for row in rd:
    row.replace('M',1)
    row.replace('F',0)


