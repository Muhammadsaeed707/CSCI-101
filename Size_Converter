"""
Assignment #2, Part 3
Muhammad Saeed
"""
#ask user for file
file = int(input("Enter a file size, in kilobytes (KB): "))
"""
Runtime Error: Not converting variable file to integer which
would lead to it not being able to be multiplied by constants as
input produces a string.
ex. file = input("Enter a file size, in kilobytes (KB): ")
"""
#line space
print ()
print (file, "KB ...")
#line space
print ()

#calculate in bits and format the decimal and commas
bits = float(file * 1024 * 8)
formatted_bits= format (bits, ',.2f')
#print and format with spaces
x= "... in bits"
y= format (x, '<26s')
"""
Syntax Error: Forgetting a closing parentheses in the
previous line. ex. y= format (x, '<26s'
"""
print (y, formatted_bits, "bits")

#calculate in bytes and format the decimal and commas
bytes1 = float(file * 1024)
formatted_bytes= format (bytes1, ',.2f')
#print and format with spaces
x= "... in bytes"
"""
Syntax Error: Forgetting a closing quotation mark
in the previous line.
ex. x="... in bytes
""" 
y= format (x, '<27s')
print (y, formatted_bytes, "bytes")

#calculate in megabytes and format the decimal
megabytes = float(file / 1024)
"""
Runtime Error: Dividing variable 'file' by 0 would cause
the program to crash.
ex. megabytes = float(file / 0)
"""
formatted_megabytes= format (megabytes, '.2f')
#print and format with spaces
x= "... in megabytes"
y= format (x, '<35s')
print (y, formatted_megabytes, "MB")

#calculate in gigabytes and format the decimal
gigabytes = float(file / 1024 / 1024)
formatted_gigabytes= format (gigabytes, '.2f')
#print and format with spaces
x= "... in gigabytes"
y= format (x, '<36s')
print (y, formatted_gigabytes, "GB")
"""
Logic Error: printing variable 'gigabytes' instead of
'formatted_gigabytes which would run but not be what i want.
ex. print (y, gigabytes, "GB")
"""
