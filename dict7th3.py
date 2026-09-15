d={1:'khushi',2:'heli',3:'hirva',4:'tulsi'}
print(d)
d[5]='jinal'
print (d)
del d[5]
print(d)
k=int(input("enter value for key:"))
if  k in d:
    print("match found")
else:
    print("match not found" ) 
for i in d.items():
    print(i)   
e={5:"parth",6:"shital"}   
d.update(e)  
print(d)
    

