import random
import sys


def getNewBoard():
    # Creates a brand new, blank board data structure.
    board = []
    for i in range(8):
        board.append(['.'] * 8)

    return board


def resetBoard(board):
    for x in range(8):
        for y in range(8):
            board[x][y] = '.'

    # Starting pieces:
    board[3][3] = 'B'
    board[3][4] = 'W'
    board[4][3] = 'W'
    board[4][4] = 'B'


def drawBoard(board):
    print('  a b c d e f g h')
    for i in range(8):
        print(i + 1, end=' ')
        for j in range(8):
            if j < 7:
                print('%s' % board[i][j], end=' ')
            else:
                print('%s' % board[i][j])


def checkMove(board, current, d):
    ch = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for i in range(8):
        for j in range(8):
            if board[i][j] == current:
                v = []
                move = []
                if i < 7:
                    a = i + 1
                    if board[a][j] != current and board[a][j] != '.':
                        while board[a][j] != current and a < 8:
                            if board[a][j] != '.':
                                move.append(str(a) + '-' + str(j))
                                if a != 7:
                                    a += 1
                                else:
                                    break
                            else:
                                move.append(str(a) + '-' + str(j))
                                r = move.copy()
                                move.clear()
                                d.setdefault(str(ch[j])+str(a+1), v).extend(r)
                                break
                v = []
                move = []
                if i > 0:
                    a = i - 1
                    if board[a][j] != current and board[a][j] != '.':
                        while board[a][j] != current and a >= 0:
                            if board[a][j] != '.':
                                move.append(str(a) + '-' + str(j))
                                if a != 0:
                                    a -= 1
                                else:
                                    break
                            else:
                                move.append(str(a) + '-' + str(j))
                                r = move.copy()
                                move.clear()
                                d.setdefault(str(ch[j])+str(a+1), v).extend(r)
                                break
                v = []
                move = []
                if j < 7:
                    a = j + 1
                    if board[i][a] != current and board[i][a] != '.':
                        while board[i][a] != current and a < 8:
                            if board[i][a] != '.':
                                move.append(str(i) + '-' + str(a))
                                if a != 7:
                                    a += 1
                                else:
                                    break
                            else:
                                move.append(str(i) + '-' + str(a))
                                r = move.copy()
                                move.clear()
                                d.setdefault(str(ch[a])+str(i+1), v).extend(r)
                                break
                v = []
                move = []
                if j > 0:
                    a = j - 1
                    if board[i][a] != current and board[i][a] != '.':
                        while board[i][a] != current and a >= 0:
                            if board[i][a] != '.':
                                move.append(str(i) + '-' + str(a))
                                if a != 0:
                                    a -= 1
                                else:
                                    break
                            else:
                                move.append(str(i) + '-' + str(a))
                                r = move.copy()
                                move.clear()
                                d.setdefault(str(ch[a])+str(i+1), v).extend(r)
                                break
                v = []
                move = []
                if j < 7 and i < 7:
                    a = i + 1
                    b = j + 1
                    if board[a][b] != current and board[a][b] != '.':
                        while board[a][b] != current and a < 8 and b < 8:
                            if board[a][b] != '.':
                                move.append(str(a) + '-' + str(b))
                                if a != 7 and b != 7:
                                    a += 1
                                    b += 1
                                else:
                                    break
                            else:
                                move.append(str(a) + '-' + str(b))
                                r = move.copy()
                                move.clear()
                                d.setdefault(str(ch[b])+str(a+1), v).extend(r)
                                break
                v = []
                move = []
                if j > 0 and i > 0:
                    a = i - 1
                    b = j - 1
                    if board[a][b] != current and board[a][b] != '.':
                        while board[a][b] != current and a >= 0 and b >= 0:
                            if board[a][b] != '.':
                                move.append(str(a) + '-' + str(b))
                                if a != 0 and b != 0:
                                    a -= 1
                                    b -= 1
                                else:
                                    break
                            else:
                                move.append(str(a) + '-' + str(b))
                                r = move.copy()
                                move.clear()
                                d.setdefault(str(ch[b])+str(a+1), v).extend(r)
                                break
                v = []
                move = []
                if j > 0 and i < 7:
                    a = i + 1
                    b = j - 1
                    if board[a][b] != current and board[a][b] != '.':
                        while board[a][b] != current and a < 8 and b >= 0:
                            if board[a][b] != '.':
                                move.append(str(a) + '-' + str(b))
                                if a != 7 and b != 0:
                                    a += 1
                                    b -= 1
                                else:
                                    break
                            else:
                                move.append(str(a) + '-' + str(b))
                                r = move.copy()
                                move.clear()
                                d.setdefault(str(ch[b])+str(a+1), v).extend(r)
                                break
                v = []
                move = []
                if j < 7 and i > 0:
                    a = i - 1
                    b = j + 1
                    if board[a][b] != current and board[a][b] != '.':
                        while board[a][b] != current and b < 8 and a >= 0:
                            if board[a][b] != '.':
                                move.append(str(a) + '-' + str(b))
                                if a != 0 and b != 7:
                                    a -= 1
                                    b += 1
                                else:
                                    if j < 7:
                                        break
                            else:
                                move.append(str(a) + '-' + str(b))
                                r = move.copy()
                                move.clear()
                                d.setdefault(str(ch[b])+str(a+1), v).extend(r)
                                break
    return ' '.join(d.keys())


def getpoint(board):
    Bpoint = 0
    Wpoint = 0
    for i in range(8):
        Bpoint += board[i].count('B')
        Wpoint += board[i].count('W')
    print('End of the game. W: '+str(Wpoint)+', B: '+str(Bpoint))
    if Bpoint > Wpoint:
        return 'B wins.'
    elif Bpoint < Wpoint:
        return 'W wins.'
    else:
        return 'Draw.'


def flip(board, dic, player, move):
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


mainBoard = getNewBoard()
resetBoard(mainBoard)
player = ['B', 'W']
i = 0
dic = {}
drawBoard(mainBoard)
while True:
    k = 0
    for j in range(8):
        if '.' in mainBoard[j]:
            k += 1
    if k > 0:
        if player[i] == 'B':
            if checkMove(mainBoard, player[i], dic) == '':
                print('Player B cannot play.')
                i += 1
                dic.clear()
            else:
                print('Valid choices:', checkMove(mainBoard, player[i], dic))
                move = input('Player B: ')
                while move not in dic.keys():
                    move = input('Invalid move choose again\nPlayer B: ')
                flip(mainBoard, dic, player[i], move)
                drawBoard(mainBoard)
                i += 1
                dic.clear()
        if player[i] == 'W':
            if checkMove(mainBoard, player[i], dic) == '':
                print('Player W cannot play.')
                i -= 1
                dic.clear()
            else:
                print('Valid choices:', checkMove(mainBoard, player[i], dic))
                move = input('Player W: ')
                while move not in dic.keys():
                    move = input('Invalid move choose again\nPlayer W: ')
                flip(mainBoard, dic, player[i], move)
                drawBoard(mainBoard)
                i -= 1
                dic.clear()
    else:
        break
print(getpoint(mainBoard))
