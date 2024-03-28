# Q3.  Leap Year Checker: Write a Python program to check if a given year is a leap year or not. If it's a leap year, print "Leap year", otherwise print "Not a leap year". (Hint: A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.)


a = int(input("Enter the year: "))

if a % 4 == 0 and a % 100 == 0 or a % 400 == 0:
	print("Leap year")
else:
	print("Not a leap year")
