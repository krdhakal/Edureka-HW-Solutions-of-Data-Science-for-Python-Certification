# Create a random array of 3 rows and 3 columns and sort it according to 1st column, 2nd column or 3rd column
import numpy as np
Z = np.random.random(9).reshape(3,3)
print Z
print np.sort(Z,axis=1)
