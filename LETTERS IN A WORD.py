#DIFFERENT LETTERS IN A WORD
def words():
    sent=input('enter a WORD ')#TAKING INPUT
    D={ }
    for ch in sent:
        if ch in D:
            D[ch]+=1#COUNTING CERTAIN LETTERS
        else:
            D[ch]=1
    for key in D:
         print(key,D[key])
words()
