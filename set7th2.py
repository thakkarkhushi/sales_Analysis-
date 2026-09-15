s1={1,2,3}
s2={6,7,3}
print(s1)
print(s2)
s1.add(4)
s2.add(9)
print(s1)
print(s2)
s1.remove(4)
s2.remove(9)
print(s1)
print(s2)
print("union",s1|s2)
print("intersection",s1&s2)
print("difference",s1-s2)
s3=s1^s2
print("symmetric difference",s3)