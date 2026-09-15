import math
def mean(list):
    n=len(list)
    mean=sum(list)/n
    print(mean)
def deviation(list):
    n=len(list)
    mean=sum(list)/n
    seq=[(x-mean)**2 for x in list]
    v=sum(seq)/n
    dev=math.sqrt(v)
    return dev
list=[1,2,3,4,5]
mean(list)
r=deviation(list)   
print(r) 
