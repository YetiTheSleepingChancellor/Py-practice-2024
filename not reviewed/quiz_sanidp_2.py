print("=====Quiz Games=====")

AnsA = '1'
Ans2 = 'b'
Ans3 = 'c'
Ans4 = 'd'

count = 0

print("""
      A.What is the first programming languages? ans is a
      
      1. Python 
      2. C programming 
      3. Pascal 
      4. ASM""")

a = int(input("Enter the answer for question 1: "))

if a >= 1 and a <= 4:
	print("invalid answer type write answers in 1, 2, 3, 4.")
else:
    a = int(input("Enter the answer for question 1: "))
    

    


print("""
      2.What is the first programming languages? Ans is b
      
      a. Python 
      b. C programming 
      c. Pascal 
      d. ASM""")

b = input("Enter the answer for question 2: ")
b = b.lower()

print("""
      3.What is the first programming languages? ans is c
      
      a. Python 
      b. C programming 
      c. Pascal 
      d. ASM""")

c = input("Enter the answer for question 3: ")
c = c.lower()

print("""
      4.What is the first programming languages? ans is d
      
      a. Python 
      b. C programming 
      c. Pascal 
      d. ASM""")

d = input("Enter the answer for question 4: ")
d = d.lower()


if a == AnsA:
    count = count + 1
    if b == Ans2:
        count = count + 1
        if c == Ans3:
            count = count + 1
            if d == Ans4:
                count = count + 1
                
        else:
            if d == Ans4:
                count = count + 1	
    else:
         if c == Ans3:
            count = count + 1
            if d == Ans4:
                count = count + 1
        
else:
    if b == Ans2:
        count = count + 1
        if c == Ans3:
            count = count + 1
            if d == Ans4:
                count = count + 1

print("Your total marks is", count ,".")
    
    



