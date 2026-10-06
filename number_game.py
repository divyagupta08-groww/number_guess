import random
playing = True
number = str(random.randint(0,9))
print("I will generate a number from 0-9")
print("you have to guess 1 number at a time")
print("good luck")
while playing:
    guess = (input("enter your number:"))
    if number==guess:
        print("you guessed it correctly")
        print(f"the number was {number}\n")
        break
    else:
        print("try again")
