# Calculate the total number of people who have a PhD degree
import numpy as np
path_to_csv='c:\\temp\\SalaryGender.csv'
arr = np.loadtxt(path_to_csv, dtype=np.object, delimiter=",", skiprows=1)
phd_count=0
phd=0
for i in range(len(arr)):
    phd = int(arr[i][3])
    if phd == 1:
        phd_count = phd_count + phd

print 'The total number of people who have a PhD degree are',phd_count


