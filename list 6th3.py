s="12203ab3"
freq = {} 
for e in s: 
    if e in freq: 
        freq[e] += 1
    else: 
        freq[e] = 1
print ("Occurrence of all characters is :\n "+ str(freq))