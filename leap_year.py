a=int(input("enter year(in four digit):"))
if a%4==0 and a%400==0 or a%100!= 0:
    print("IT IS AN LEAP YEAR")
else:
    print("NOT AN LEAP YEAR")