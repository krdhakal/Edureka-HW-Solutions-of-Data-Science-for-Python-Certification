# Create a random matrix and Compute a matrix rank
import numpy as np
Z = np.random.uniform(0,1,(10,10))
U, S, V = np.linalg.svd(Z)
rank = np.sum(S > 1e-10)
print rank
