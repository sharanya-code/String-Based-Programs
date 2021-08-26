#TO CHECK A PALLINDROME A WORD
def words():
    word=input('enter a word')
    flag=1
    L=len(word)
    for i in range (0,L//2):
        if (word[i]!=word[L-i-1]):#CHECKS IF THE SAME LETTER COMES AT THE SAME POSITION FROM BOTH SIDES
            flag=0
            break
            
    if flag==1:
        print('it is a pallindrome')
        
    else:
        print('not a pallindrome')
words()
