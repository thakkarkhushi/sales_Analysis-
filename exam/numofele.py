l=[1,2,3,3,4,4,5,6,3]
c={}
for i in l:
    if i in c:
        c[i]+=1
    else:
        c[i]=1    
print("occourrence of each digit in list are",c)
