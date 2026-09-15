c=0
while(c< 127):
    print(chr(c),"hexa=",hex(c),"decimal:",int(c),end=" ")
    c=c+1
    if c%5==0:
        print("\n")     