"""
Assignment #3, Part 3
Muhammad Saeed
"""
#ask user to input and define variables
month = int(input("Enter a month (1-12): "))
day = int(input("Enter a day (1-31): "))

#convert numeric answers to months
if month == 1:
    month1 = ("January")
elif month == 2:
    month2 = ("February")
elif month == 3:
    month3 = ("March")
elif month == 4:
    month4 = ("April")
elif month == 5:
    month5 = ("May")
elif month == 6:
    month6 = ("June")
elif month == 7:
    month7 = ("July")
elif month == 8:
    month8 = ("August")
elif month == 9:
    month9 = ("September")
elif month == 10:
    month10 = ("October")
elif month == 11:
    month11 = ("November")
elif month == 12:
    month12 = ("December")

#set range of invalid dates
if month <= 0 or day <= 0:
    print ("That's not a valid date!")
elif month <= 0 or day > 31:
    print ("That's not a valid date!")
elif month > 12 or day <= 0:
    print ("That's not a valid date!")
elif month > 12 or day > 31:
    print ("That's not a valid date!")
else:
    #set dates for breaks
    if month == 2 and day == 18:
        print ("February 18 is Presidents' Day. No classes scheduled / University Holiday.")
    elif month == 3 and day == 18:
        print ("March 18 is Spring Recess. No classes scheduled / University Holiday.")
    elif month == 3 and day == 19:
        print ("March 19 is Spring Recess. No classes scheduled / University Holiday.")
    elif month == 3 and day == 20:
        print ("March 20 is Spring Recess. No classes scheduled / University Holiday.")
    elif month == 3 and day == 21:
        print ("March 21 is Spring Recess. No classes scheduled / University Holiday.")
    elif month == 3 and day == 22:
        print ("March 22 is Spring Recess. No classes scheduled / University Holiday.")
    elif month == 3 and day == 23:
        print ("March 23 is Spring Recess. No classes scheduled / University Holiday.")
    elif month == 3 and day == 24:
        print ("March 24 is Spring Recess. No classes scheduled / University Holiday.")
    else:
        #set dates for before and after the semester
        if month == 1 and day < 28:
            print (month1, day, "is before the start of the Spring 2019 term.")
        elif month == 5 and day > 21:
            print (month5, day, "is after the end of the Spring 2019 term.")
        elif month == 6:
            print (month6, day, "is after the end of the Spring 2019 term.")
        elif month == 7:
            print (month7, day, "is after the end of the Spring 2019 term.")
        elif month == 8:
            print (month8, day, "is after the end of the Spring 2019 term.")
        elif month == 9:
            print (month9, day, "is before the start of the Spring 2019 term.")
        elif month == 10:
            print (month10, day, "is before the start of the Spring 2019 term.")
        elif month == 11:
            print (month11, day, "is before the start of the Spring 2019 term.")
        elif month == 12:
            print (month12, day, "is before the start of the Spring 2019 term.")
        else:
            #set dates for normal school days
            if month == 1:
                print (month1, day, "is not a school holiday at NYU.  The university is open.")
            elif month == 2:
                print (month2, day, "is not a school holiday at NYU.  The university is open.")
            elif month == 3:
                print (month3, day, "is not a school holiday at NYU.  The university is open.")
            elif month == 4:
                print (month4, day, "is not a school holiday at NYU.  The university is open.")
            elif month == 5:
                print (month5, day, "is not a school holiday at NYU.  The university is open.")
        
            
                
