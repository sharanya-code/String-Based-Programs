#PROGRAM TO CHECK THE NUMBER OF WORDS IN A SENTANCE
def word():
    sent=input('enter a sentance')
    L=len(sent)
    count=1
    for ch in range(0,L):
        if (sent[ch]==" "):
            count+=1
            
    print('number of words=',count)
word()
