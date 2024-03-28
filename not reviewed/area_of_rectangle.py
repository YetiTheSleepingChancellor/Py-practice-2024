# 1.Write a Python program to calculate the area of a rectangle. Prompt the user to enter the length and width of the rectangle as input.
# the inputs are changed to integer because the area of rectangle cannot be in other data type. maybe not it could be in float. but here we only want user to use integer otherwise the user might input other data types that we don't want.

l = int(input("Enter the lenght of the rectangle in meter: "))
w = int(input("Enter the width of the rectangle in meter: "))

print(l*w,"sq.m")