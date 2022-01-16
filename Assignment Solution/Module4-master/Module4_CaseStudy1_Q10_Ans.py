# Create numpy array having elements 0 to 10 And negate all the elements between 3 and 9
import numpy
arr=numpy.arange(11)
print arr
index=[3,9]
new_arr = numpy.delete(arr,index)
print new_arr