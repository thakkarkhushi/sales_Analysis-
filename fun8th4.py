def emi(loan_amount,year,interest):
    interest=interest/(12*100)
    no_of_months=year*12
    emi=(loan_amount*interest*(1+interest)**no_of_months)/((1+interest)**no_of_months-1)
    total=emi*no_of_months
    print("emi=",emi)
    print("total payment=",total)
loan_amount=float(input("enter loan amonut:"))
year=float(input("enter no of year:")) 
interest=float(input("enter rate of interest:"))
emi(loan_amount,year,interest)   