n=int(input("enter size:"))
list=[]
for i in range(0,n):
    a=int(input("enter an value:"))
    list.append(a)
print(list)   
p=0
neg=0
z=0
for i in range (len(list)):
    if list[i]>0:
        p=p+1
    elif list[i]<0:
        n=n+1
    elif list[i]==0:
        z=z+1
print("postive:",p)
print("negitive:",neg)
print("zero :",z)
e=0
o=0
for i in range (len(list)):
    if list[i]%2==0:
        e=e+1
    else:
        o=o+1    
print("even=",e)
print("odd=",o) 
sum=0
for i in range (len(list)):
    sum=list[i]+sum
avg=sum/n
print("averge of all number:",avg)    


