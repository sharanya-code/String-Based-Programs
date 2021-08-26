#COUNT THE NUMBER OF UPPERCASE AND LOWERCASE LETTERS
def upper():
      sent=input("Enter string:")
      count1=0
      count2=0
      for i in sent:
            if(i.islower()):#COUNT THE NUMBER OF LOWERCASE LETTERS
                count1=count1+1
                
            elif(i.isupper()):#COUNT THE NUMBERS OF UPPERCASE LETTERS
                  count2=count2+1
                  
      print("NUMBER OF LOWERCASE LETTERS:")
      print(count1)

      print("NUMBER OF UPPERCASE LETTERS:")
      print(count2)
upper()
