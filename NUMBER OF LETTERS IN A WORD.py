#NUMBER OF LETTERS IN A WORD
string = input("Please enter your own String : ")
char = input("Please enter your own Character : ")

count = 0
for i in range(len(string)):#CHECKING IF A LETTER IS IN A GIVEN STRING
    if(string[i] == char):#COUNTING THE TIMES OS HAS OCCURRED
        count = count + 1

print(" Number of Times ", char, " has Occurred = " , count)
