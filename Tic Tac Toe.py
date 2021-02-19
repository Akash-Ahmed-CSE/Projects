board = {
    'A': ' ', 'B':' ', 'C':' ',
    'D': ' ', 'E':' ', 'F':' ',
    'G': ' ', 'H':' ', 'I':' '
}

player = 1          #initial first player
total_moves = 0     #count the moves
end_check = 0

def check ():
    # checking the moves of player one
    # for horizontal(start)
    if board['A'] == 'X' and board['B'] == 'X' and board['C'] == 'X':
        print('Player one won !')
        return 1
    if board['D'] == 'X' and board['E'] == 'X' and board['F'] == 'X':
        print('Player One Won!!')
        return 1
    if board['G'] == 'X' and board['H'] == 'X' and board['I'] == 'X':
        print('Player One Won!!')
        return 1
    # for horizontal(end)

    # for diagonal(start)
    if board['A'] == 'X' and board['E'] == 'X' and board['I'] == 'X':
        print('Player One Won!!')
        return 1
    if board['C'] == 'X' and board['E'] == 'X' and board['G'] == 'X':
        print('Player One Won!!')
        return 1
    # for diagonal(end)

    # for vertical(start)
    if board['A'] == 'X' and board['D'] == 'X' and board['G'] == 'X':
        print('Player One Won!!')
        return 1
    if board['B'] == 'X' and board['E'] == 'X' and board['H'] == 'X':
        print('Player One Won!!')
        return 1
    if board['C'] == 'X' and board['F'] == 'X' and board['I'] == 'X':
        print('Player One Won!!')
        return 1
    # for vertical(end)

    # checking the moves of player two
    # for horizontal(start)
    if board['A'] == 'X' and board['B'] == 'X' and board['C'] == 'X':
        print('Player one won !')
        return 1
    if board['D'] == 'X' and board['E'] == 'X' and board['F'] == 'X':
        print('Player One Won!!')
        return 1
    if board['G'] == 'X' and board['H'] == 'X' and board['I'] == 'X':
        print('Player One Won!!')
        return 1
    # for horizontal(end)

    # for diagonal(start)
    if board['A'] == 'O' and board['E'] == 'O' and board['I'] == 'O':
        print('Player One Won!!')
        return 1
    if board['C'] == 'O' and board['E'] == 'O' and board['G'] == 'O':
        print('Player One Won!!')
        return 1
    # for diagonal(end)

    # for vertical(start)
    if board['A'] == 'O' and board['D'] == 'O' and board['G'] == 'O':
        print('Player One Won!!')
        return 1
    if board['B'] == 'O' and board['E'] == 'O' and board['H'] == 'O':
        print('Player One Won!!')
        return 1
    if board['C'] == 'O' and board['F'] == 'O' and board['I'] == 'O':
        print('Player Two Won!!')
        return 1
    return 0
    # for vertical(end)



print('****************************')
print('** Welcome to Tic Tac Toe **')
print('****************************')

print('A|B|C')
print('-+-+-')
print('D|E|F')
print('-+-+-')
print('G|H|I')
print('**************************')

while True:
    print(board['A']+'|'+board['B']+'|'+board['C'])
    print('-+-+-')
    print(board['D']+'|'+board['E']+'|'+board['F'])
    print('-+-+-')
    print(board['G']+'|'+board['H']+'|'+board['I'])
    end_check = check()

    if total_moves == 9 or end_check ==1:
        break
    while True:             #input from players
        if player == 1:     #choose player
            p1_input = input('player one :')
            if p1_input.upper() in board and board[p1_input.upper()] == ' ':
                board[p1_input.upper()] ='X'
                player = 2
                break

            else:                   #on wrong in put
                print('Invalide input try again!')
                continue
        else:
            p2_input = input('Player two:')
            if p2_input.upper() in board and board[p2_input.upper()] == ' ':
                board[p2_input.upper()] ='O'
                player = 1
                break

            else:                   #on wrong in put
                print('Invalide input try again!')
                continue
    total_moves+=1
    print('*******************************************')
    print()
