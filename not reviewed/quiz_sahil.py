# question
#variable
score = 0

print("""
      
      A. Who is the first programmer

      a. lady ada lovence
      b. thomos adition
      c. denis ritchee
      d. binod khadka""")

ans1 =  input("Enter the ans1: ").lower()
if ans1 >= 'a' and ans1 <= 'd':
    if ans1 == 'a':
        score+=1
    else:
         ans1 =  input("Enter the ans1: ").lower()
else:
    ans1 =  input("Enter the ans1: ").lower()
   
print("""
      B. who  is the father of computer?

      a. lady ada lovence
      b. chales babbage
      c. denis ritchee
      d. binod khadka""")

ans2 = input("Enter the ans2: ").lower()
if ans2 >= 'a' and ans2 <= 'd':
    if ans2 == 'b':
        score+=1
    else:
        ans2 =  input("Enter the ans2: ").lower()
else:
    ans2 =  input("Enter the ans2: ").lower()

print("""
      C. who  is the father linux?

      a. lady ada lovence
      b. chales babbage
      c. linux torval
      d. binod khadka""")

ans3 = input("Enter the ans3: ").lower()
if ans3 >= 'a' and ans3 <= 'd':
     if ans3 == 'c':
        score+=1
     else:
          ans3 =  input("Give ans in (a,b,c,d) the ans3: ").lower()
else:
    ans3 =  input("Give ans in (a,b,c,d) the ans3: ").lower()

print("Your score  is ",score)