import random

board = ['-'] * 9
cross = 'X'
zero = 'O'
gameRunning = True
winner = None
count = 0
random_number = 0

def display_board(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('----------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('----------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])



def player_input(board):
    player = int(input('Enter a number 1-9: '))
    if player >= 1 and player <= 9 and board [player - 1] == '-':
        board[player - 1] = cross
    

def check_win(board):
    global gameRunning
    global winner
    # Horizontal Check
    if board[0] == board[1] == board[2] and board[1] != '-':
        winner = board[0]
        gameRunning = False
    elif board[3] == board[4] == board[5] and board[4] != '-':
        winner = board[3]
        gameRunning = False
    elif board[6] == board[7] == board[8] and board[7] != '-':
        winner = board[6]
        gameRunning = False
    # Vertical Check
    elif board[0] == board[3] == board[6] and board[3] != '-':
        winner = board[0]
        gameRunning = False
    elif board[1] == board[4] == board[7] and board[4] != '-':
        winner = board[1]
        gameRunning = False
    elif board[2] == board[5] == board[8] and board[5] != '-':
        winner = board[2]
        gameRunning = False
    # Diagonal Check
    elif board[0] == board[4] == board[8] and board[4] != '-':
        winner = board[0]
        gameRunning = False
    elif board[2] == board[4] == board[6] and board[4] != '-':
        winner = board[2]
        gameRunning = False
    
    # check Tie
    elif '-' not in board:
        print('It is a tie')
        gameRunning = False

def switchPlayer():
    if board[random_number] == '-':
        board[random_number] = zero
    else:
        randomNumber()
        board[random_number] = zero

def randomNumber():
    global random_number
    random_number = random.randint(0, 8)

    


def play():
    display_board(board)
    check_win(board)
    if count % 2 == 0:
         player_input(board)
    else:
        switchPlayer()
        

while gameRunning:
    play()
    count += 1

