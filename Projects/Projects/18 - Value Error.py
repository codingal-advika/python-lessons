# try:
#     UserInput = input('Enter a number: ')
#     print('You have entered ' , UserInput)
#     if UserInput.isdigit() != True:
#         UserNumber = int(UserInput)
#     else:
#          UserNumber = int(UserInput)
#     if (UserNumber % 2 )== 0 :
#         print('Your number is even.') 
#     else:
#         print('Your number is odd.')
# except ValueError as ex:
#     print("The input you entered is incorrect. Please enter a valid number")
    
try:
    UserInput = input('Enter a number: ')
    print('You have entered ' , UserInput)
    
    if UserInput.isdigit() == True:
        userNumber = int(UserInput)
        
        if (userNumber % 2 )== 0 :
            print('Your number is even.')
        else:
            print('Your number is odd.')
    else:
         print('Your input is not a number. Please enter a valid number.')
    
except ValueError as ex:
    print("The input you entered is incorrect. Please enter a valid number")
    
 