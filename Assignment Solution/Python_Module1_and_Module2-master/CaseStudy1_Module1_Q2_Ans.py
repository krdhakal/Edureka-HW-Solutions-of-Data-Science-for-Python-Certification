'''
Q2. Write a code which accepts a sequence of words as input and
    prints the words in a sequence after sorting them alphabetically.
'''
print("Enter comma separated words in a sequence:")
list=[n for n in input().split(',')]
list.sort()
print("Sorted:")
print(','.join(list))
