cause = input('Do you have a medical cause? Enter Y or N: ')
if cause == 'Y' :
    print('You are eligible to take the exam')
else:
    attendence = int(input('Enter your attendence'))
    if attendence < 75 :
        print('You are not eligible to take the exam')
    else:
        print('You are eligible to take the exam')
