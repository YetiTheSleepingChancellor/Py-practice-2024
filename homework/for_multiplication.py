
# ask the user for until which no you want the multiplicaiton from. 
print("Enter the multiplication you want: ", end="")
a = int(input())
b = 1


while b <= a:
    for x in range(1, 11):
        print(b,"x", x, "=", b*x)
    b+=1
    print()


# # Ask the user for until which number they want the multiplication tables
# a = int(input("Enter the multiplication you want: "))

# # Generate multiplication tables up to the entered number
# for b in range(1, a + 1):
#     for x in range(1, 11):
#         print(b, "x", x, "=", b * x)
#     print()
