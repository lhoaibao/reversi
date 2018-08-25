import random
import sys
def getNewBoard():
    board = []
    for i in range(8):
        board.append(['.']*8)
    return board

def resetBoard(board):
    for i in range(8):
        for j in range(8):
            board[i][j] = '.'
    board[3][3] = 'W'
    board[3][4] = 'B'
    board[4][3] = 'B'
    board[4][4] = 'W'

def drawBoard(board):
    print('  a b c d e f g h')
    for i in range(8):
        print(i + 1, end='')
        for j in range(8):
            if j < 7:
                print(' %s' %board[i][j], end=' ')
            else:
                print(' %s' %board[i][j])



def enterPlayerTile():
    # Lets the player type which tile they want to be.
    # Returns a list with the player's tile as the first item, and the computer's tile as the second.
    tile = ''
    while not (tile == 'W' or tile == 'B'):
        print('Do you want to be W or B?')
        tile = input().upper()

    # the first element in the tuple is the player's tile, the second is the computer's tile.
    if tile == 'W':
        return ['W', 'B']
    else:
        return ['B', 'W']

def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


print('Welcome to Reversi!')

mainBoard = getNewBoard()
resetBoard(mainBoard)
playerTile, computerTile = enterPlayerTile()
turn = whoGoesFirst()
print('The' + turn + 'will go first.')

drawBoard(mainBoard)
