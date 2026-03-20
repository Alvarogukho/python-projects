import random



def valuecreator():
    randnum = random.randint(1,100)
    return randnum


while True:
        randnum = valuecreator()
        while True:
            guess = int(input("Guess a number from 1 to 100 : "))

            if guess == randnum:
                print("You Win!!")
                break
            elif guess <= randnum:
                print("Higher")
            elif guess >= randnum:
                print("Lower")
    
