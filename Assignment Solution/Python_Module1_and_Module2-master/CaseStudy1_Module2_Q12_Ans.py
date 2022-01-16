# Please write a program which count and print the numbers of each character in a string input by console.
# Example string: abcdefgabc

str=raw_input('Enter a string:')
list = list(str)
unique = set(list)

for val in unique:
    print val, str.count(val)