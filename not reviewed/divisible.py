# 2. Create a Python program that asks the user to input a number and then prints whether it's is divisible by 4 or not.

a = int(input("Enter a number: "))

if a % 4 == 0:
	print("Divisible by 4.")
else:
	print("Not divisible by 4.")