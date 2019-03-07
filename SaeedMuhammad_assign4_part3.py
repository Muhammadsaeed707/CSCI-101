"""
Assignment #4, Problem 3
Muhammad Saeed
"""
#Arrow Display
#ask user for columns
#ask user for direction


while True:
    columns = int(input("How many columns? "))
    direction = input("Direction? (l)eft or (r)ight: ")
    #make sure entries are valid
    if columns <= 0:
        print ("Invalid entry, try again!")
    elif direction != "l" and direction != "r":
        print ("Invalid entry, try again!")
    else:
        break
    
#what to do if direction is right 
if direction == "r":

    #set spaces to begin
    spaces = 0

    #while loop for spaces and * in foreward slash
    while True:
        print(" "* spaces,"*")
        #add spaces everytime 
        spaces += 1
        #when spaces greater than column break
        if spaces >= columns:
            break

    #set spaces to begin the other way  
    spaces = columns - 2

    #while loop for spaces and * in backward slash
    while True:
        print(" "* spaces,"*")
        #subtract spaces everytime
        spaces -= 1
        #when spaces equal -1 then break
        if spaces == -1:
            break

#what to do if direction is left 
elif direction == "l":
    
    #set spaces to begin
    spaces = columns - 1

    #while loop for spaces and * in backward slash
    while True:
        print(" "* spaces,"*")
        #subtract spaces everytime
        spaces -= 1
        #when spaces equal 0 then break
        if spaces == 0:
            break

    #set spaces to begin the other way 
    spaces = 0

    #while loop for spaces and * in foreward slash
    while True:
        print(" "* spaces,"*")
        #add spaces everytime
        spaces += 1
        #when spaces greater than column break
        if spaces >= columns:
            break


