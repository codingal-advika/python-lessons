import os 
def shutdown_system():
    y ='yes'
    n = 'No'
    userInput = input('Would you like to shutdown or not? Enter yes or no: ')
    if userInput == y :
        print('Shutting down the system')
        os.system('shutdown /s /t 10')
    else :
        print('Shutdown cancelled.')
    

shutdown_system()