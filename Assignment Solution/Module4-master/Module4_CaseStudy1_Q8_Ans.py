# Create  a  10x10  array  with  random  values  and  find the  minimum  and  maximum values.
import numpy
arr=numpy.random.randint(10, size=10)
print 'Array',arr
print 'Minimum value in the array is',arr.min()
print 'Maximum value in the array is',arr.max()