"""
Assignment #3, Part 1
Muhammad Saeed
"""
#Valid Triangle Tester
#In order to see if user inputed side lengths make an valid triangle
#header
print ("Valid Triangle Tester")
#enter 3 points
point1x = float(input("Enter Point #1 - x position: "))
point1y = float(input("Enter Point #1 - y position: "))
point2x = float(input("Enter Point #2 - x position: "))
point2y = float(input("Enter Point #2 - y position: "))
point3x = float(input("Enter Point #3 - x position: "))
point3y = float(input("Enter Point #3 - y position: "))
#line space
print ()
#distances
side1 = ((point1x-point2x)**2 + (point1y-point2y)**2)**0.5
side2 = ((point2x-point3x)**2 + (point2y-point3y)**2)**0.5
side3 = ((point1x-point3x)**2 + (point1y-point3y)**2)**0.5
#format distances to 2 decimals
formatted_side1 = format(side1, '.2f')
formatted_side2 = format(side2, '.2f')
formatted_side3 = format(side3, '.2f')
#print side lenghts
print ("The length of each side of your test shape is: ")
print ("Side 1:", formatted_side1)
print ("Side 2:", formatted_side2)
print ("Side 3:", formatted_side3)
print ()
#if statements to see if valid triangle or not 
if (side1+side2)>side3 and (side2+side3)>side1 and (side1+side3)>side2:
    print ("This is a valid triangle!")
else:
    print ("This is not a valid triangle")

