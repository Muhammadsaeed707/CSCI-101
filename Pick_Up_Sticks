
"""
Assignment #4, Problem 2
Muhammad Saeed
"""
#Game of Pick Up Sticks
# user input for starting sticks between 1-3
loop = True
while loop:
    sticks = int(input("How many sticks are on the table? (enter a number between 10 and 100): "))
    if sticks <= 9:
        print("Invalid # of sticks, please try again.")
    elif sticks >= 101:
        print("Invalid # of sticks, please try again.")
    else:
        break

print()

# game start
while True:
    turn = 1
    # first players turns
    while turn == 1:
        print("There are", sticks, "sticks on the table.")
        print("Turn: Player 1")
        remove = int(input("How many sticks do you want to remove from the table? (1, 2 or 3):"))
        #make sure enter valid number
        if remove < 1 or remove > 3:
            print("Invalid number of sticks, try again.")
            print()
        elif sticks == 2 and remove > 2:
            print("You can't take that many sticks off of the table. Try again.")
            print()
        elif sticks == 1 and remove > 1:
            print("You can't take that many sticks off of the table. Try again.")
            print()
        else:
            if sticks != remove:
                print() 
            break
    # remove sticks from table
    sticks -= remove
    # add 1 to turn to switch players
    turn += 1
    # check if game is over
    #subtract 1 to turn to find loser
    if sticks == 0:
        turn_final = turn - 1 
        break
    
    # second players turns
    while turn == 2:
        print("There are", sticks,"sticks on the table.")
        print("Turn: Player 2")
        remove = int(input("How many sticks do you want to remove from the table? (1, 2 or 3):"))
        #make sure stick number is valid
        if remove < 1 or remove > 3:
            print("Invalid number of sticks, try again.")
            print()
        elif sticks == 2 and remove > 2:
            print("You can't take that many sticks off of the table. Try again.")
            print()
        elif sticks == 1 and remove > 1:
            print("You can't take that many sticks off of the table. Try again.")
            print()
        else:
            if sticks != remove:
                print()
            break
    # remove requested sticks from table
    sticks -= remove
    # subtract 1 to switch to player 1 turn
    turn -= 1
    #check if game is over
    #add 1 to turn to find loser
    if sticks == 0:
        turn_final = turn + 1
        break
 
#game ends declare loser
print ("Player",turn_final,"loses!")

    
