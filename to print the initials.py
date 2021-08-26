#TO ONLY PRINT INITIALS OF A PHRASE
def initial():
    word=input('enter a phrase')
    L=len(word)
    print(word[0],end='')
    for i in range(0,L):
        if (word[i]==" "):#CHECKS FOR SPACE AND PRINTS THE NEXT LETTER
            print(word[i+1],end='')
initial()
