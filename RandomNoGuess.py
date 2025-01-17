import random

target=random.randint(1,100)

while True:
    userChoice= input("Guess the target from 1 to 100 or QUIT(Q): ")
    if (userChoice=="Q"):
        break
    userChoice=int(userChoice)
    if (userChoice==target):
        print("Yes, you guessed it correctly")
        break
    elif (userChoice < target):
        print("Your input target is smaller try guessing bigger number ")
    elif (userChoice > target):
        print("Your input target is bigger try guessing smaller number ")
        

print("Game finished")
