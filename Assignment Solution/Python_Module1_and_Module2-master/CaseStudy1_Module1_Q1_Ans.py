# Q1. Write a program which will find factors of given number and find whether the factor is even or odd.
def get_factors(x):
   print("Factors of", x ,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           j=check_even_odd(i)  
           print(str(i)+j)

def check_even_odd(x):
    if (x % 2 == 0):
        return (" and it's an Even number")
    else:
        return (" and it's an Odd number")

givennum = int(input("Enter a number: "))
get_factors(givennum)
