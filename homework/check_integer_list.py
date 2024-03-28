# check and find the integer if in the list and display there is an integer if there is.

list = ["hari", "shyam", "manish", "binod", "alex", 5]

for x in list:
    a = type(x)
    print(a)

    if a == int:
        print("The index" "is a integer. Which is", a)
    else: 
        print("There is no integer in the list")


# list = ["hari", "shyam", "manish", "binod", "alex", 5]

# found_integer = False  # Flag to track if an integer is found in the list

# for x in list:
#     if isinstance(x, int):  # Check if the element is an integer
#         found_integer = True
#         print("There is an integer in the list. It is:", x)
#         break  # Stop iteration once an integer is found

# if not found_integer:
#     print("There is no integer in the list")
