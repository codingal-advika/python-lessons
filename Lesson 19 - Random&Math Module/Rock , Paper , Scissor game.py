import random
while True :
    print('Lets play Rock Paper Scissor shoot with the computer! ')
    user = input('Enter a option from the following.Rock,Paper,Scissors: ')
    options = ['Rock' , 'Paper' , 'Scissors']
    com = random.choice(options)
    print('You chose ' , user ,  'computer chose ' , com)
   
    if user==com :
            print('Its a tie!')
    elif user == 'Rock':
        if com == 'Paper' :
            print('Paper defeats rock!Computer wins!!!')
        else:
             print('Rock beats scissors!You won!!!')
    elif user == 'Paper':
        if com == 'Scissors' :
            print('Scissors defeats rock!Computer wins!!!')
        else:
            print('Paper beats Rock!You won!!!')
    elif user == 'Scissors':
        if com == 'Paper' :
             print('Rock defeats Scissors!Computer wins!!!')
        else:
            print('Scissors beats Paper!You won!!!')
    again = input('Would you like to play again : ')
    if again != 'y':
        break
    
        

    

