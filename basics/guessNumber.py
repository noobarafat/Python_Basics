from random import randint

for x in range(1, 6):
    guessNUmber = int(input("ENter your guess between 1 to 5:"))
    randomNumber =randint(1, 5)

    if guessNUmber == randomNumber:
        print("You have won")
    
    else:
        print("You have lost")
        print("Random number was: ", randomNumber)