import string
def main():
    file=input("enter file name:")
    infile=open(file,'r')
    outer=input("enter the name of the file to write to:")
    outfile=open(outer,'w')
    for i in infile:
        words=i.split( )
        for word in words:
            counter=0
            for letter in word:
                if not i in string.punctuation:
                    counter +=1
                if counter  == 4:
                        word="****"
            print(word +" ",file=outfile,end="")           
    infile.close()
    outfile.close()     
if __name__=="__main__" :
     main()
              
