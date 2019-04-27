import random
import time
name = input("Hello, what is your name?")


time.sleep(1)
print("Hello" + ' ' + name + ',' + "I am thinking of a number between 1 and 10")


time.sleep(1)
print("You only have 3 tries!")
the_number = random.randint(1, 10)
tries = 1
guess = int(input("Take a guess: "))


while guess != the_number:
    if guess < 10 and guess > the_number:
        print("Number is lower")
    elif guess > 10:
        tries += 1
        print("Oops, enter a number between 1 and 10")
    elif tries == 3:w
        break
    elif guess < the_number:
        print("Number is higher")

    try:
        guess = int(input("Take a guess: "))
        tries += 1
    except ValueError:
        print("Oops, enter a number")



if guess == the_number:
    print("You guessed it!  The number was", the_number)
    time.sleep(1)
    print("And it only took you", tries, "tries!")
    input("Press the enter key to exit.")

if tries == 3:
    print("You Lose!!")
    input("Press the enter key to exit.")








