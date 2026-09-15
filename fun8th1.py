import random
def suffle(l1):
    random.shuffle(l1)
    return l1
l1=[1,2,3,4,5,6,7]
s=suffle(l1)
print(s)