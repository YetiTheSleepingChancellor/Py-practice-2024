# Write a Python script that asks the user for a password. If the password is "password123", print "Access granted", otherwise print "Access denied".

# Steps:
# Ask the user for the input.
# check if the user input password is "password123"
# if the password is "password123" then grant access otherwise deny.

print()
print("Enter the password:", end="")
user_input = input()

if user_input == "password123":
	print("Access granted.")
else: 
	print("Access denied.")  