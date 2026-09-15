rev=0
n=int(input("enter number to revese:"))
while n> 0:
  r=n%10
  rev=(rev*10)+r
  n=n//10
print("reverse number is:",rev)  