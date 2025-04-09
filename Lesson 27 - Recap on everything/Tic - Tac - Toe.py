Board = {'1': '' , '2': '' , '3': '' ,
         '4': '' , '5': '' , '6': '' ,
        '7': '' ,'8': '' , '9': '' }
board_keys = []

for key in Board:
    board_keys.append(key)

def printBoard(b):
    print(b['1'] + '|' + b['2'] + '|' + b['3'])
    print('-+-+-')
    print(b['4'] + '|' + b['5'] + '|' + b['6'])
    print('-+-+-')
    print(b['7'] + '|' + b['8'] + '|' + b['9'])


def Tic_tac_toe():
    turn = input('Enter x or 0:')
    count = ''
    if turn.lower() == 'x':
        turn = 0
    else:
        turn = 'x'
    for i in range(10) :
        printBoard(Board)
        print('Its your turn!' + turn + 'Where do you want to move?')
        move = input('Type a number from the grid: ')
        if Board[move] == '':
            Board [move] = turn
        else:
            ('That place has already been filled pleace enter another number')    
        if count >=5:
            if Board['1'] == Board['2'] == Board['3'] != '' :
                printBoard(Board)
                print('Game over')
                print('****' + turn + 'won.****')
                break
            elif Board['4'] == Board['5'] == Board['6'] != '' :
                printBoard(Board)
                print('Game over')
                print('****' + turn + 'won.****')
                break
            elif Board['7'] == Board['8'] == Board['9'] != '' :
                printBoard(Board)
                print('Game over')
                print('****' + turn + 'won.****')
                break
            elif Board['1'] == Board['4'] == Board['7'] != '' :
                printBoard(Board)
                print('Game over')
                print('****' + turn + 'won.****')
                break
            elif Board['2'] == Board['5'] == Board['8'] != '' :
                printBoard(Board)
                print('Game over')
                print('****' + turn + 'won.****')
                break
            elif Board['3'] == Board['6'] == Board['9'] != '' :
                printBoard(Board)
                print('Game over')
                print('****' + turn + 'won.****')
                break
            elif Board['1'] == Board['5'] == Board['9'] != '' :
                printBoard(Board)
                print('Game over')
                print('****' + turn + 'won.****')
                break
            elif Board['3'] == Board['5'] == Board['7'] != '' :
                printBoard(Board)
                print('Game over')
                print('****' + turn + 'won.****')
                break
        if count == 9:
            print('It is a tie!')   

        if turn == 'x' or 'X':
            turn == '0'
        else:
            turn == 'x' or 'X'

    restart = input('Do you want to play again? yes or no:')
    if restart == 'yes' or restart == 'Yes':
        for key in board_keys:
            Board[key] = ''
        Tic_tac_toe()