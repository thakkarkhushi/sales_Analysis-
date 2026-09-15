c=int(input(print("choose an option to find area \n 1.circle \n 2.triangle \n 3.ractangle \n 4.square:")))
if c==1:
  pi=3.14
  a=int(input("enter radius:"))
  area=pi*a*a
  print("area of circle is:",area)
elif c==2:
 q=0.5
 e=int(input("enter hight:")) 
 b=int(input("enter base:"))
 k=q*e*b
 print("arae of triangle is:",k) 
elif c==3:
  l=int(input("enter length:"))  
  w=int(input("enter width:"))
  o=l*w
  print("area of ractangle is:",o)
elif c==4:
  x=int(input("enter length:"))
  d=x*x
  print("area of sqaure:",d)
else:
  print("NO OPERATION")  