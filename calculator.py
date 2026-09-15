print("WELCOME TO THE CALCULATOR")
a=int(input("enter number:"))
b=int(input("enter anthorn number:"))
c=int(input(" choose an operation \n 1.addition \n 2.subtraction \n 3.multiplication \n 4. division \n 5. modulor \n 6.power \n 7.quotient\n"))
if (c==1):
    res=a+b
    print("addition is:",res)
elif(c==2):
    res=a-b
    print("subtaraction is:",res)
elif(c==3):
    res=a*b
    print("multiplication is:",res)
elif(c==4):
    res=a/b
    print("division is:",res)
elif(c==5):
    res=a%b
    print("modular is:",res)  
elif(c==6):
    res=a**b
    print("division is:",res)
elif(c==7):
    res=a//b
    print("division is:",res)
else:
    print("NO OPERATION")              


            