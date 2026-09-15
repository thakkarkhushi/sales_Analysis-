file=input("enter file name:")
f=open(file,'r')
data=f.read()
words=data.split()
sen=data.split(",")
total_word=0
total_sentences=0
for word in words:
    total_word+=len(words)
for s in sen:
    total_sentences+=len(sen)    
W=total_word/len(words)  
c=total_sentences/len(sen)
print("avg word:",W)
print("avg sentences:",c)      