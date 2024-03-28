# Homework Question:
# You are tasked with creating a password hashing system. Here's how the code should operate:

# Generate a hash key.
# Prompt the user to enter a password.
# Modify the password by adding a specific number to each character.
# Hash the modified password.
# If a user inputs the correct hash, display the original password.
# Hints use : ord() and chr()


hash_pass = 65

a = input("Enter the password: ").upper()

b = ord(a)
print(b)

if b == hash_pass:
    print("The hash password is",hash_pass)
else:
    print("Invalid")

