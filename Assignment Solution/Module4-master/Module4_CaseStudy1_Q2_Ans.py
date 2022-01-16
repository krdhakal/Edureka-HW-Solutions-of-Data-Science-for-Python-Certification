# The number of men with a PhD
# The number of women with a PhD
import numpy as np
path_to_csv='c:\\temp\\SalaryGender.csv'
arr = np.loadtxt(path_to_csv, dtype=np.object, delimiter=",", skiprows=1)

number_of_men_with_phd=0
number_of_women_with_phd=0
gender=0
phd=0

for i in range(len(arr)):
    gender = int(arr[i][1])
    phd = int(arr[i][3])
    if phd == 1 & gender == 1:
        number_of_men_with_phd = number_of_men_with_phd + phd
    else:
        number_of_women_with_phd = number_of_women_with_phd + phd

print 'The number of men with a PhD:',number_of_men_with_phd,'\nThe number of women with a PhD:',number_of_women_with_phd


