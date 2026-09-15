s=25
e=60
print("prime num between",s,"and",e,"are:")
for i in range(s,e+1):
    if i>1:
        for j in range(2,i):
            if(i%j)==0:
                break
        else:
            print(i)



        
