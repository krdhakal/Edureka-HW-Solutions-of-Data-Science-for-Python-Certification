#Design a code which will find the given number is Palindrome number or not.
n=int(input("Enter a number:"))
temp=n
rev=0
while(n>0):
    q = n%10
    rev = rev*10+q
    n = n//10
if(temp == rev):
    print("%d is a palindrome number" % temp)
else:
    print("%d is not a palindrome number" % temp)

