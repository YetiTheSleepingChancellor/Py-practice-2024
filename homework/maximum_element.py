# WAP to find the maximum element in list.

# Define the list
my_list = [5, 20, 25, 8, 12, 10]

# Initialize max_element with the first element of the list
max_element = my_list[0]

# Iterate through the list to find the maximum element
for element in my_list:
    if element > max_element:
        max_element = element

# Print the maximum element
print("The maximum element in the list is:", max_element)
