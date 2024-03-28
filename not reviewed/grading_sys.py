
# Q2.  Grading System: Create a Python program that takes a student's score as input and prints their grade. Use the following grading scale:

# 90 or above: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F

a = int(input("Enter your score: "))

if a >= 90:
	print("A")
elif a >= 80:
	print("B")
elif a >= 70:
	print("C")
elif a >= 60:
	print("D")
else:
	print("F")
