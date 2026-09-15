import random
def game(ch):
    list=[0,1,2]
    c=random.choice(list)
    while True:
        if ch==c:
            print("draw")
        if ch==1 and c==0:
            print("you win")
        else:
            print("you lose")
        if ch==2 and c==1:
            print("you win")
        else:
            print("you lose")
        if ch==0 and c==2:
            print("you win")
        else:
            print("you lose") 
        break    
ch=int(input(" \n0 is for scissor\n1 is for roack\n2 is for paper\nenter your choice:"))
game(ch)             


        