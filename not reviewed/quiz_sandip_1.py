# question
#variable
score = 0

print("""
      
      A. What is the first programmer

      a. lady ada lovence
      b. thomos adition
      c. denis ritchee
      d. binod khadka""")

ans1 =  input("Enter the ans: ").lower()
if ans1 == 'a':
    score += 1
   
print("""
      B. who  is the father computer?

      a. lady ada lovence
      b. chales babbage
      c. denis ritchee
      d. binod khadka""")

ans2 = input("Enter the ans: ").lower()
if ans2 ==  'b':
    score+=1

print("""
      C. who  is the father linux?

      a. lady ada lovence
      b. chales babbage
      c. linux torval
      d. binod khadka""")

ans3 = input("Enter the ans: ").lower()
if ans3 ==  'c':
    score+=1

print("Your score  is ",score)







