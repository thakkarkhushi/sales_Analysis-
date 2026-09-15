def remove_dup(list):
    dup=[]
    for i in list:
        if i not in dup:
            dup.append(i)    
    return(dup)  
list=[1,2,3,4,4,5,5]  
l=remove_dup(list)
print(l)


