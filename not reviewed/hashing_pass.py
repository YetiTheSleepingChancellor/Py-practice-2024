
# Homework Question:
# You are tasked with creating a password hashing system. Here's how the code should operate:

# Generate a hash key.
# Prompt the user to enter a password.
# Modify the password by adding a specific number to each character.
# Hash the modified password.
# If a user inputs the correct hash, display the original password.
# Hints use : ord() and chr()

# password  -> Get from User
# Hash ma change garnu
# Display
# you want to decript the password Y n N ?
# if Y -> change to password
# No -> leave


# hash = #hashed of the password.

# a = input("Enter the password: ")

# b = #convert to hash the password given by the user.

# if b == hash:
#     print("access Granted")
# else:
#     print("Access denide")

pwssed = input("Enter the password: ")

temp= ord(pwssed[0]) / 5

new_pass = int(temp)

new_pass = chr(new_pass)

print(new_pass, end ="")

print(pwssed[1], end ="")
print(pwssed[2], end ="")
print(pwssed[3], end ="")


# pwssed[0] = new_pass

# print(pwssed)