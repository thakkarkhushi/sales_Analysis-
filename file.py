"""f=open("word.txt","x")
if f:
    print("file creted")"""
f=open("word.txt","w")
f.write('this file is demo file\n')
f.write("hello")
f.close()
f=open("word.txt","r")
tx=f.read()
print(tx)
f.close()
"""f=open("file1","x")"""
f=open("file1.txt","w")
f.write("hello word")
f.close()
"""f=open("file2","x")"""
f=open("file2.txt","w")
f.write("sky is the linit")
f.close()