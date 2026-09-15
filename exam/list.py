l=[0,1,3,4,5]
l2=[0,32,77,45,5]
c=0
for i in l:
    for j in l2:
        if i==j:
            c=c+1
print(" number of common element are:",c)
"""sum=0
for i in l:
    sum=sum+i
print(sum)    
l2=[]
for i in l:
    if i not in l2:
        l2.append(i)
print(l2)
print(l)        
print(l)
l.insert(2,2)
print(l)
l.append(6)
print(l)
l.remove(6)
print(l)
del l[0]
print(l)
i={7,8,9,10}
l.extend(i)
print(l)"""