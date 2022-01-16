# Create a numpy array [[0, 1, 2],[ 3, 4, 5],[ 6, 7, 8],[ 9,10, 11]] and filter the elements greater than 5

import numpy
arr=numpy.array([[0, 1, 2],[3, 4, 5],[6, 7, 8],[9,10, 11]])
x=arr>5
print 'Main Array',arr
print 'Greater than 5',x
print 'Greater than 5 elements',arr[x]
