'''
Q3. Write a program, which will find all the numbers between 1000 and 3000 (both included)
such that each digit of a number is an even number.
The numbers obtained should be printed in a comma separated sequence on a single line.
'''
output = []

for num in range(1000, 3001):

    str1 = str(num)
    strLen = len(str1)

    if (int(str1[0]) % 2 == 0) and (int(str1[1]) % 2 == 0) and (int(str1[2]) % 2 == 0) and (int(str1[3]) % 2 == 0):
        output.append(str1)

print(",".join(output))