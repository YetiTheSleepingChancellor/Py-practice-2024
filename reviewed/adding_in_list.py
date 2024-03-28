# make empty list
# input n from user n -> int
# loop run till n and add element
# print list

lst = []
print()
print("Enter no of element you want in list:", end="")
size_of_lst = int(input())
i =  0

if size_of_lst <= 5:  
    while i<size_of_lst:
        print("Enter the", i+1,"th element:", end="")
        b =  input()
        lst.append(b)
        i += 1
    print(lst)
else:
    print("Your size should be less or equal to 5")

if "sahil" in lst:
    sahil_ind = lst.index("sahil")
    del lst[sahil_ind]
else:
    lst.append("sahil")
print(lst)








