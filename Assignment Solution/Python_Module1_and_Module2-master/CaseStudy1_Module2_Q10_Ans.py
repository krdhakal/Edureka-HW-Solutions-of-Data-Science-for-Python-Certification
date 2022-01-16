#Please write a program which accepts a string from console and print the characters that have even indexes.
str=raw_input('Enter a string:')
result = ""
for i in range(len(str)):
    if i%2==0:
        result = result + str[i]

print result


