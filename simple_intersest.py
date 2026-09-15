import math
p=int(input("enter principal:"))
r=int(input("enter rate of interest:"))
t=int(input("enter time:"))
n=int(input("enter number of time interest applied:"))
si=p*r*t/100
print("simple interest:",si)
a=1+(r/(100*n))
c=p*math.pow(a,n*t)
print("compound interest:",c)