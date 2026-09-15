s=2
n=int(input("enter number for series:"))
sum=0
for i in range(1,n+1):
    print(s,end=" ")
    sum=sum+s
    s=s*10+2
print("\rsum of series:",sum)    
