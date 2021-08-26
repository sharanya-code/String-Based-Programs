import random

options = ["Rock","Paper","Scissors"]
h=random.randint(0,2)
c=options[h]
user=input("Pick either Rock, Paper or Scissors: ")
user=user.lower()
if user == 'rock' or 'paper' or 'scissors':
    print('The computer has drawn',c)
    print('You have chosen',user)
if user == 'rock':
    if c == 'Rock':
        print ('Tie Game')
    elif c == 'Paper':
        print ('AI Wins')
    else:
        print ('User Wins')
if user == 'paper':
    if c == 'Rock':
        print ('User Wins')
    elif c == 'Paper':
        print ('Tie Game')
    else:
        print ('AI Wins')
if user == 'scissors':
    if c == 'Rock':
        print ('AI Wins')
    elif c == 'Paper':
        print ('User Wins')
    else:
        print ('Tie Game')

