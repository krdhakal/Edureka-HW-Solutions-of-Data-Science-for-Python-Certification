# Write  a  program  to  compute  1/2+2/3+3/4+...+n/n+1  with  a  given  n  input  by console (n>0)
num=int(raw_input('Enter a number:'))
result=0
for i in range(1,num+1):
    result += float(float(i)/(i+1))
print result