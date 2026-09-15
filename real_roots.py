import math
print("To find real roots")
a=int(input("enter first value:"))
b=int(input("enter second value:"))
c=int(input("enter third value:"))
d=(b*b)-(4*a*c)
if d==0:
    print("two equal roots")
elif d<0:
    print("no real roots")
elif d>0:
    print("two real roots")
    x=math.sqrt(d)
    r=((-b)+x)/(2*a)
    r2=((-b)-x)/(2*a)
    print(" 1st real root is:",r)
    print(" 2nd real root is:",r2)

 