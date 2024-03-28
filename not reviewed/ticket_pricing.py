# Q4.  Ticket Pricing: Create a Python program that asks the user for their age and determines the ticket price for a movie. If the age is below 18, the ticket price is $8. If the age is between 18 and 65 (inclusive), the ticket price is $12. For seniors (age 65 and above), the ticket price is $6.


a = int(input("Enter your age: "))

if a < 18:
	print("The ticket price is $8")
elif a >= 18 and a <= 65:
	print("The ticket price is $12")	
else:
	print("The ticket price is $6")
