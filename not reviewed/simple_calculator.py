print("=====Simple Calculator=====")


a = int(input("Enter the first number: "))
c = input("Enter the operator +, -, *, /: ")
b = int(input("Enter the Second number: "))



if c == '+':
    print(a+b)
elif c == '-':
	print(a-b)
elif c == '*':
	print(a*b)
elif c == '/':
	print(a/b)   
else:
	print("Invalid Operator.")