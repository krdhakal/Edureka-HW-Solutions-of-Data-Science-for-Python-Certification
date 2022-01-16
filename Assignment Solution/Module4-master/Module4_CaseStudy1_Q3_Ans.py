# Store the Age and PhD columns in one DataFrame and delete the data of all people who dont have a PhD
import numpy as np
path_to_csv='c:\\temp\\SalaryGender.csv'
A = np.loadtxt(path_to_csv, dtype=np.object, delimiter=",", skiprows=1)
print A[:, [2, 3]][A[:, 3] == 1]