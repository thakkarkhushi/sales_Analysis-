sum=0
for i in range(1,10000+1):
    sum=0
    for j in range (1,i):
        if(i%j==0):
            sum=sum+j
    if(i==sum):
        print("perfact number is:",i)
