dict={'gujarat':'gandhinager','andhra pradesh':'amaravati','assam':'dispur','goa':'panji'}
while True:
    state=input("enter state(write exit to quit):")
    if state=='exit':
        break
    if state in dict:
        cap=input("enter capital:")
        if cap==dict[state]:
            print('correct')
        else:
            print('incorrect')    
    else:
        print("state not found")