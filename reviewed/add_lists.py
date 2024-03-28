
a = ["manish", "sandip", "kumar", "sahil", 5, 6]
b = ["man", "san", "kum", "sa"]
c = ["don", "bun", "horn", "corn", "torn"]

n = len(a) #len() function will find the length of the list a

if n % 2 == 0:
    a.extend(b) # add the list b to a
    a.extend(c) # add the list c to a
else:
    a.append("object") #adds element at the last of the list

print(a)






