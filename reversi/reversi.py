import random
import sys
mainBoard = [['.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', 'W', 'B', '.', '.', '.'],
['.', '.', '.', 'B', 'W', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.']]


def drawBoard(board):
    print('  a b c d e f g h')
    for i in range(8):
        print(i + 1, end=' ')
        for j in range(8):
            if j < 7:
                print('%s' %board[i][j], end=' ')
            else:
                print('%s' %board[i][j])

def checkMove(board,current,dic):
    char = ['a','b','c','d','e','f','g','h']
    for i in range(8):
        for j in range(8):
            if board[i][j] == current:
                move = []
                if i < 7:
                    a = i + 1
                    if board[a][j] != current and board[a][j] != '.':
                        while board[a][j] != current and a < 7:
                            if board[a][j] != '.':
                                move.append(str(a) + '-' +str(j))
                                a += 1
                            else:
                                move.append(str(a) + '-' +str(j))
                                moveResult = move.copy()
                                move.clear()
                                dic.setdefault(str(char[j])+str(a+1),moveResult)
                                break
                move = []
                if i > 0:
                    a = i - 1
                    if board[a][j] != current and board[a][j] != '.':
                        while board[a][j] != current and a > 0:
                            if board[a][j] != '.':
                                move.append(str(a) + '-' +str(j))
                                a -= 1
                            else:
                                move.append(str(a) + '-' +str(j))
                                moveResult = move.copy()
                                move.clear()
                                dic.setdefault(str(char[j])+str(a+1), moveResult)
                                break
                move = []
                if j < 7:
                    a = j + 1
                    if board[i][a] != current and board[i][a] != '.':
                        while board[i][a] != current and a < 7:
                            if board[i][a] != '.':
                                move.append(str(i) + '-' +str(a))
                                a += 1
                            else:
                                move.append(str(i) + '-' +str(a))
                                moveResult = move.copy()
                                move.clear()
                                dic.setdefault(str(char[a])+str(i+1), moveResult)
                                break
                move = []
                if j > 0:
                    a = j - 1
                    if board[i][a] != current and board[i][a] != '.':
                        while board[i][a] != current and a > 0:
                            if board[i][a] != '.':
                                move.append(str(i) + '-' +str(a))
                                a -= 1
                            else:
                                move.append(str(i) + '-' +str(a))
                                moveResult = move.copy()
                                move.clear()
                                dic.setdefault(str(char[a])+str(i+1), moveResult)
                                break
                move = []
                if j < 7 and i < 7:
                    a = i + 1
                    b = j + 1
                    if board[a][b] != current and board[a][b] != '.':
                        while board[a][b] != current and a < 7 and b < 7:
                            if board[a][b] != '.':
                                move.append(str(a) + '-' +str(b))
                                a += 1
                                b += 1
                            else:
                                move.append(str(a) + '-' +str(b))
                                moveResult = move.copy()
                                move.clear()
                                dic.setdefault(str(char[b])+str(a+1), moveResult)
                                break
                move = []
                if j > 0 and i > 0:
                    a = i - 1
                    b = j - 1
                    if board[a][b] != current and board[a][b] != '.':
                        while board[a][b] != current and a > 0 and b > 0:
                            if board[a][b] != '.':
                                move.append(str(a) + ' -' +str(b))
                                a -= 1
                                b -= 1
                            else:
                                move.append(str(a) + '-' +str(b))
                                moveResult = move.copy()
                                move.clear()
                                dic.setdefault(str(char[b])+str(a+1), moveResult)
                                break
                move = []
                if j > 0 and i < 7:
                    a = i + 1
                    b = j - 1
                    if board[a][b] != current and board[a][b] != '.':
                        while board[a][b] != current and a < 7 and b > 0:
                            if board[a][b] != '.':
                                move.append(str(a) + '-' +str(b))
                                a += 1
                                b -= 1
                            else:
                                move.append(str(a) + '-' +str(b))
                                moveResult = move.copy()
                                move.clear()
                                dic.setdefault(str(char[b])+str(a+1), moveResult)
                                break
                move = []
                if j < 7 and i > 0:
                    a = i - 1
                    b = j + 1
                    if board[a][b] != current and board[a][b] != '.':
                        while board[a][b] != current and b < 7 and a > 0:
                            if board[a][b] != '.':
                                move.append(str(a) + '-' +str(b))
                                a -= 1
                                b += 1
                            else:
                                move.append(str(a) + '-' +str(b))
                                moveResult = move.copy()
                                move.clear() 
                                dic.setdefault(str(char[b])+str(a+1), moveResult)
                                break
    return ' '.join(dic.keys())

def getpoint(board):
    Bpoint = 0
    Wpoint = 0
    for i in range(8):
        Bpoint += board[i].count('B')
        Wpoint += board[i].count('W')
    print('End of the game. W: '+Wpoint+', B: '+Bpoint)
    if Bpoint > Wpoint:
        return 'B wins.'
    elif Bpoint < Wpoint:
        return 'W wins.'
    else:
        return 'Draw.'

def flip(board,dic,player,move):
    if player == 'B':
        x = dic.get(move)
        for i in range(len(x)):
            x[i] = x[i].split('-')
            board[int(x[i][0])][int(x[i][1])] = 'B'
    else:
        x = dic.get(move)
        for i in range(len(x)):
            x[i] = x[i].split('-')
            board[int(x[i][0])][int(x[i][1])] = 'W'
    return board

player = ['B','W']
i = 0
k = 0
dic = {}
drawBoard(mainBoard)
while True:
    for j in range(8):
        if '.' in mainBoard[j]:
            k += 1
    if k > 0:
        if player[i] == 'B':
            if checkMove(mainBoard,player[i],dic) == '':
                print('Player B cannot play.')
                i += 1
                dic.clear()
            else:
                print('Valid choices:',checkMove(mainBoard,player[i],dic))
                move = input('Player B: ')
                while move not in dic.keys():
                     move = input('Invalid move choose again\nPlayer B: ')
                flip(mainBoard,dic,player[i],move)
                drawBoard(mainBoard)
                i += 1
                dic.clear()
        if player[i] == 'W':
            if checkMove(mainBoard,player[i],dic) == '':
                print('Player B cannot play.')
                i += 1
                dic.clear()
            else:
                print('Valid choices:',checkMove(mainBoard,player[i],dic))
                move = input('Player W: ')
                while move not in dic.keys():
                     move = input('Invalid move choose again\nPlayer W: ')
                flip(mainBoard,dic,player[i],move)
                drawBoard(mainBoard)
                i -= 1
                dic.clear()
    else:
        break
print(getpoint(mainBoard))
