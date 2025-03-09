import os 
y  ='yes'
n = 'no'
shutdown = input('Would you like to shutdown or not? Enter yes or no: ')
s = os.system('shutdown/s/t/5')
if shutdown == y :
    
else:
    print('Shut down cancelled.')