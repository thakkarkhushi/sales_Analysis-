"""f=open("abc.txt","x")
y=open("abc.txt","w")
y.write("my name is khushi\n")
y.write("this is text file")
w=open("abc.txt",'w')
w.write("welcom! ")
w.close()
y=open("abc.txt",'a')
y.write(" To the python programming")
y.close()"""
f=open('abc.txt',"w")
l=['hello\n','writing multiline string\n','this is third line\n']
f.writelines(l)
f.close()
e=open('abc.txt',"r")
x=e.read()
print(x)
e.close()

