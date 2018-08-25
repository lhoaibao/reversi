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
        print(i + 1, end=' ')
        for j in range(8):
            if j < 7:
                print('%s' %board[i][j], end=' ')
            else:
                print('%s' %board[i][j])

def checkMove(board,current):
    dic = {}
    move = []
    char = ['a','b','c','d','e','f','g','h']
    for i in range(8):
        for j in range(8):
            if board[i][j] == current:
                a = i + 1
                if board[a][j] != current and board[a][j] != '.':
                    a = i + 1
                    while board[a][j] != current and a < 7:
                        if board[a][j] != '.':
                            move.append(str(char[j])+str(a+1))
                            a += 1
                        else:
                            move.append(str(char[j])+str(a+1))
                            moveResult = move.copy()
                            move.clear()
                            dic.setdefault(moveResult[len(moveResult) - 1], []).append(moveResult[0:len(moveResult)])
                            break

    return ' '.join(dic.keys())
mainBoard = getNewBoard()
resetBoard(mainBoard)
end = False
player = ['B','W']
i = 0
print(checkMove(mainBoard,'B'))
while end == True:
    if '.' not in mainBoard:
        break
    else:
        if player[i] == 'B':
            drawBoard(mainBoard)
            checkMove(mainBoard,player[i])
            move = input()
            while move not in dic.keys():
                 move = input()
            k = dic.get(move)
            for j in range(len(k)):
                mainBoard[k[j][0]][k[j][1]] = 'B'
            drawBoard(mainBoard)
            i += 1
        if player[i] == 'W':
            drawBoard(mainBoard)
            checkMove(mainBoard,player[i])
            move = input()
            while move not in dic.keys():
                 move = input()
            k = dic.get(move)
            for j in range(len(k)):
                mainBoard[int(k[j][0])][int(k[j][1])] = 'W'
            drawBoard(mainBoard)
            i -= 1


#tra diem
