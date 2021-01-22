"""
Assignment #2, Part 2
Muhammad Saeed
"""
#ask user name and classes and store in variable
name = input("What is your name? ")
class1 = input("What class are you in? ")
#line space
print ()
#ask how much tests are worth and store in variable as float
test_worth = float(input("How much are tests worth in this class (i.e. 0.40 for 40%): "))
#ask for tests scores and store in variable as integers
test1 = int(input ("Enter test score #1: "))
test2 = int(input ("Enter test score #2: "))
test3 = int(input ("Enter test score #3: "))
#line space
print ()
#calculate, format, and display test average
test_average = ((test1 + test2 + test3) / 300) * 100
formatted_test_average = format (test_average, '.2f')
print ("Your test average is:",formatted_test_average)
#line space
print ()
#ask how much hw is worth and store in variable as float
hw_worth = float(input("How much are homework assignments worth in this class (i.e. 0.60 for 60%): "))
#ask for homework scores and store in variable as integers
hw1 = int(input("Enter homework score #1: "))
hw2 = int(input("Enter homework score #2: "))
hw3 = int(input("Enter homework score #3: "))
#line space
print ()
#calculate, format, and display homework average
hw_average = ((hw1 + hw2 + hw3) / 300) * 100
formatted_hw_average = format (hw_average, '.1f')
print ("Your homework average is:",formatted_hw_average)
#line space
print ()
#closing statement 
#calculate, format, and display final grade 
final_grade = ((hw_average * hw_worth) + (test_average * test_worth))
formatted_final_grade = format (final_grade, '.2f')
print ("Thanks, ",name,". Your final score in ", class1, " is ", formatted_final_grade, sep="")
