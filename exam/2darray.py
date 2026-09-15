import random
l=[[random.choice(0,1)],[1,0,0,0],[0,1,1,0],[1,0,0,1]]
a=0
b=0
i=0
j=0
for i in l:
    for j in i:
        if j==0:
            a=a+1
        if j==1:
            b=b+1
print('number of 1:',b)
print('number of 0:',a)      
   