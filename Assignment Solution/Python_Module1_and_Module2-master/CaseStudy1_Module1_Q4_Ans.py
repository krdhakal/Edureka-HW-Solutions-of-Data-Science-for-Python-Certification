'''
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose if the entered string is:

Python0325
Then the output will be:
LETTERS: 6
DIGITS: 4
'''
import re
str1=input("Enter alpha numeric work.")
r = re.compile("([a-zA-Z]+)([0-9]+)")
m = r.match(str1)
print("String value is", m.group(1))
print("Numaric value is", m.group(2))