"""n=int(input("enter number for multipication table:"))      
for j in range(1,10):
    print(n,"*",j,"=",n*j)
l=[1,2,3,4,5,6,7,8,9,10]
for i in l:
    print(l[i])
n= int(input("enter number:"))
c=0
while(n!=0):
    n=n//10
    c=c+1
print("count is:",c)
w=(input("enter word to check:"))
r=w[::-1]
if(w==r):
    print("it is")
else:
    print("its not")
s=int(input("enter start of series:")) 
e=int(input("enter end of series:")) 
for i in range(s,e+1):
    if(i%2 !=0):
        print(i)
odd=0
even=0
s=int(input("enter start of series:")) 
e=int(input("enter end of series:")) 
for i in range(s,e+1):
    if(i%2 !=0):
        odd=odd+1
    else:
        even=even+1  
print("odd num in series:",odd)
print("even num of series:",even)
n1=0
n2=1
while(n2==50):
    r=n1+n2
    n1=n2
    n2=rk
    print(r)
str="khushi"
i=input("enter letter to search:")
if i not in str:
    print("yes")
else:
    print("no")
list=[1,2,3,4,5,6,7]
for i in list:
    print(list[i])
x=len(list)    
while i<x:
    print(list[i])
    i=i+1
def max(a,b):
    if a>b:
        print(a,"is max number")
    else:
        print(b,"is max number")
max(7,3)
max(3,8)
import math  
def fun():
    for i in range(1,6):
        if i%2==0:
            c=math.sqrt(i)
            print(c)
fun()  
def num():
    count=0
    for i in range(1,21) :
        if i%5==0:
            count=count+1
    print(count)       
num()             

def dun(x):
    if x%2 ==0:
        print("even")
    else:
        print("odd")
dun(3)
dun(8) 
a=int(input("enter an number:"))
b=int(input("enter an anthor number:"))
if a>b:
    print(a,'is greater than ',b)
elif a==b:
    print("both are same")    
else:
    print(b,'is greater than',a)
for i in range(1,11):
    print(i)
    i=i+1   
i=1
while i<11:
    print(i)
    i=i+1 
for i in range(0,5):
    for j in range(0,i+1):
        print("*",end =" ")
    print()
i=0  
j=0
while i<6:
    while j<i:
        print("*",end=" ")
        j=j+1
    j=0
    i=i+1
    print() 
num=1
for i in range(1,6):
    for j in range(1,i+1):
        print(num,end=" ")
    num=num+1    
    print()"""

        




