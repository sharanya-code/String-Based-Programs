s = input("Enter the String 1 : ")
k = input("Enter the String 2 : ")
       
k = k.lower()
s = s.lower()
count = 0
for i in s:
    if i not in k:
        count = 1
        break
    else:
        count = 0
if count == 1:
    print("No")
elif count == 0:
    print("Yes")
