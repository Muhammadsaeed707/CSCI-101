"""
Assignment #4, Problem 1
Muhammad Saeed
"""
#Random needed for random number pick
import random 

#ask for input in while loop
#also make sure greater than 3

while True:
    dice = int(input("How many sides on your dice? "))
    if dice < 0:
        print ("Sorry, that's not a valid size value. Please choose a positive number.")
    elif dice >= 0 and dice <= 3:
        print("Sorry, that's not a valid size value. Please choose a number greater than 3.")
    #continue with code
    else:
        print ()
        print("Thanks! Here we go ...")
        print ()
        #break loop when it ends 
        break

#set variables for attempts, dice 1 and 2, and doubles starting at 0 
attempts = 0
dice1 = 0
dice2 = 0 
doubles = 0
 
while True:
    #while loop for number 1 and 2 being randomized
    num1 = random.randint(1, dice)
    num2 = random.randint(1, dice)
    
    #attempts to go up everytime
    attempts += 1
    
    #print results
    print (attempts,". die number 1 is ", num1, " and die number 2 is ", num2, ".", sep="")
    
    #dice 1 and 2 to be added to numbers 1 and 2
    dice1 += num1
    dice2 += num2

    #check for doubles
    if num1 == num2:
        
        #if find double add 1
        doubles += 1
        
    #check for snake eyes
    if num1 == num2 and num1 == 1:
        print ()
        #results for snake eyes and how many attemts
        print ("You got snake eyes! Finally! On try number ", attempts, "!", sep="")
        #results for how many doubles
        print ("Along the way you rolled double(s)", doubles, "times")
        #results for average rolls
        print ("The average roll for die #1 was", format(dice1/attempts, '.2f'))
        print ("The average roll for die #2 was", format(dice2/attempts, '.2f'))
        #break when ends 
        break
