h=int(input("enter your height(in m):"))
w=int(input("enter your waight(in kg):"))
h1=h*h
bmi=w/h
if bmi>=19 and bmi<=25:
    print("person is healty")
elif bmi>19:
    print("person is underwaight") 
elif bmi<25:
    print("person is overwaight")            