import random
att=0
number= random.randint(1,100)
print("\n Welcome to NUMBER GUESSING GAME!!")
print("\n You have guess number between 1 to 100")
while True:
    guess=int(input("Enter your guess(Within given Range):"))
    att+=1
    if guess<number:
        print("Too low!! Try again")
    elif guess>number:
        print("Too high!! Try again")
    else:
        print(f"Correct!! The Number was{number}")
        print(f"you guessed it in{att} attempts")
        break
