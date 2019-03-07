"""
Assignment #3, Part 2
Muhammad Saeed
"""
#Guess the Number Game
#get random number
import random
number = random.randint(1,10)
#print header
print("I'm thinking of a number between 1 and 10!")
#ask user for guess
guess1 = int(input("What's your guess? "))
#if statements for guess 1 possibilities 
if guess1 == number:
    #if user guesses number
    print ("You got it!")
    print ("The secret number was ", number,".", sep="")
    print ("It took you 1 try to guess the number.")
elif guess1 > number:
    print ("Too high try again.")
    #if statements for if guess 1 is too high
    #user prompted to enter guess 2
    guess2 = int(input("What's your guess? "))
    if guess2 == number:
        #if user guesses number
        print ("You got it!")
        print ("The secret number was ", number,".", sep="")
        print ("It took you 2 tries to guess the number.")
    elif guess2 > number:
        #if statements for if guess 2 is too high
        #user prompted to enter guess 3
        print ("Too high try again.")
        guess3 = int(input("What's your guess? "))
        #guess 3 possibilities 
        if guess3 == number:
            #if user guesses number
            print ("You got it!")
            print ("The secret number was ", number,".", sep="")
            print ("It took you 3 tries to guess the number.")
        elif guess3 > number:
            print ("The secret number was ", number,".", sep="")
            print ("You didn't guess the number.")
        else:
            guess3 > number
            print ("The secret number was ", number,".", sep="")
            print ("You didn't guess the number.")
    else:
        guess2 < number
        #if statements for if guess 2 is too low
        #user prompted to enter guess 3
        print ("Too low, try again.")
        guess3 = int(input("What's your guess? "))
        #guess 3 possibilities
        if guess3 == number:
            #if user guesses number
            print ("You got it!")
            print ("The secret number was ", number,".", sep="")
            print ("It took you 3 tries to guess the number.")
        elif guess3 > number:
            print ("The secret number was ", number,".", sep="")
            print ("You didn't guess the number.")
        else:
            guess3 > number
            print ("The secret number was ", number,".", sep="")
            print ("You didn't guess the number.")
else:
    guess1 < number
    #if statements for if guess 1 is too low
    #user prompted to enter guess 2
    print ("Too low, try again.")
    guess2 = int(input("What's your guess? "))
    if guess2 == number:
        #if user guesses number
        print ("You got it!")
        print ("The secret number was ", number,".", sep="")
        print ("It took you 2 tries to guess the number.")
    elif guess2 > number:
        #if statements for if guess 2 is too high
        #user prompted to enter guess 3
        print ("Too high try again.")
        guess3 = int(input("What's your guess? "))
        #guess 3 possibilities
        if guess3 == number:
            #if user guesses number
            print ("You got it!")
            print ("The secret number was ", number,".", sep="")
            print ("It took you 3 tries to guess the number.")
        elif guess3 > number:
            print ("The secret number was ", number,".", sep="")
            print ("You didn't guess the number.")
        else:
            guess3 > number
            print ("The secret number was ", number,".", sep="")
            print ("You didn't guess the number.")
    else:
        guess2 < number
        #if statements for if guess 2 is too low
        #user prompted to enter guess 3
        print ("Too low, try again.")
        guess3 = int(input("What's your guess? "))
        #guess 3 possibilities
        if guess3 == number:
            #if user guesses number
            print ("You got it!")
            print ("The secret number was ", number,".", sep="")
            print ("It took you 3 tries to guess the number.")
        elif guess3 > number:
            print ("The secret number was ", number,".", sep="")
            print ("You didn't guess the number.")
        else:
            guess3 > number
            print ("The secret number was ", number,".", sep="")
            print ("You didn't guess the number.")

        
