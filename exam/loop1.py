"""for i in range(0,5):
    for j in range(0,i+1):
        print( "*" ,end = " ")
    print()  
num=1
for i in range (0,5):
    for j in range(0,i+1):
        print(num ,end =" ")
    num=num+1
    print()
for i in range (6,1,-1):
    for j in range(i-1,1,-1):
        print(" ",end="")
    for j in range(7,i,-1):
        print("* ",end="")
    print()
"""
n=5
i=0
for i in range(1,6):
    print(" "*(5-i)+"*"*i)
    i=i+1
for i in range (6,1,-1):
    for j in range(i-1,1,-1):
        print(" ", end="")
    for j in range(7,i,-1):
        print("* ",end="") 
    print() 
"""i=0
num=0     
for i in range (1,6):
    print(" "*(i-5)+num*i)
    i=i+1
    num=num+1
    print()
p=int(input("enter principal amount:"))
r=int(input("enter rate of interst:"))
t=int(input("enter time:"))
si=(p*r*t)/100
print("simple interst:",si)
n=int(input("enter number:"))
sum=0
for i in range(1,n+1):
    r=1/(2*i-1)
    sum=sum+r
print("sum is",sum)"""
for i in range(6):
    for k in range(0,5-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()        



