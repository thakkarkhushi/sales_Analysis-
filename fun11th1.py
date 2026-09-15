"""f=open("file.txt","x")
print(f)
if f:
    print("file created")"""
f=open("file.txt","w")
f.write("hello everyone\n")
f.write("this is python program\n")
f.close()
f=open("file.txt","r")
tx=f.readline()
print(tx)
f.close()
f=open("file.txt","r")
tx=f.read()
print(tx)
f.close()
f=open("file.txt","w")
f.write("adding new string\n")
f.close()
f=open("file.txt","r")
tx=f.readline()
print(tx)
f.close()

t=["khushi","jinal","rensi"]
with open ("file.txt",'w') as fp:
    for i in t:
        fp.write("%s\n"%i)
f=open("file.txt","r")
tx=f.read()
print(tx)
f.close()

count=0
with open('file.txt','r') as fp:
    for count,line in enumerate(fp):
        pass
print("lines ",count+1)
with open("file.txt") as file:
    c=file.read()
    w=c.split()
    wc=len(w)
    print(wc)
f=open("file.txt","r")
tx=f.read()
print(tx)
f.close()    