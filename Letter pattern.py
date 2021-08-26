number = 65
num = int(input("Enter the number of rows: "))
for i in range(0,num):
    print('\n')
    for j in range(0,i+1):
        print (chr(number),end  = " " )
        number = number + 1
