# By using list comprehension, please write a program to print the list after removing
# the value 24 in [12,24,35,24,88,120,155]

list1 = [12,24,35,24,88,120,155]
for i in range(list1.count(24)):
    list1.remove(24)

print list1
