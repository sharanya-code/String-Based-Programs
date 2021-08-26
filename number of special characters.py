#NUMBER OF SPECIAL CHARACTERS IN A STRING
def sent():
    s=input('ENTER A STRING')
    count=0
    sm=0
    for i in s:
        if i in ('AEIOUaeiou'):#TO COUNT NUMBER OF VOWELS
            count+=1
    print('the number of vowels are ', count)

    for j in s:
        if j in ('!@#$%^&*()-_+={}[]:;"<>?,./1234567890'):#TO COUNT NUMBER OF SPECIAL CHARACTERS
            sm=sm+1

    print('the number of special characters are ',sm)        
        
sent()
    
