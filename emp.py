a=int(input("enter a numbers of hours you have worked:"))
if a<40:
    c=a*35
    print("amount of payment is:",c)
else:
    q=(a-40)
    d=(40*35)+(q*45)
    print("amount of payment is:",d)
