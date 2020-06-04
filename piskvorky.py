from os import system, name

def clear(): 
  
    if name == 'nt': 
        _ = system('cls') 

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

positions = [ (25,25),  (125, 25), (225,25), 
             (25,125), (125,125), (225,125),
             (25,225), (125,225), (225,225)]


#def printBoard(board):


def checkRows(board):
    if (board[0] == board[1] == board[2] != "-") or (board[3] == board[4] == board[5] != "-") or (board[6] == board[7] == board[8] != "-"):
        return 1
    else:
        return 0

def checkCols(board):
    if (board[0] == board[3] == board[6] != "-") or (board[1] == board[4] == board[7] != "-") or (board[2] == board[5] == board[8] != "-"):
        return 1
    else:
        return 0

def checkDiag(board):
    if (board[0] == board[4] == board[8] != "-") or (board[2] == board[4] == board[6] != "-"):
        return 1
    else:
        return 0

def checkWin(board):
    if checkRows(board) or checkCols(board) or checkDiag(board): 
        return 1
    else:
        return 0

def checkTie(board):
    if "-" not in board:
        return 1
    else:
       return 0

def moveTo(board, player):

    pos = int(input("Hrac " + player + " zadaj poziciu: "))

    while pos < 1 and pos > 9:	
    	pos = int(input("Hrac " + player + " zadaj poziciu: "))

    if player == "X":

        if board[pos - 1] == "-":
            board[pos - 1] = "X"
        else:
            moveTo(board, player)

    if player == "O":

        if board[pos - 1] == "-":
            board[pos - 1] = "O"
        else:
            moveTo(board, player)

def game(board):
    printBoard(board)
    flag = "-"

    while checkWin(board) == 0 and checkTie(board) == 0:

        moveTo(board, "X")
        if checkWin(board):
            flag = "X"
            break

        if checkTie(board):
            break

        moveTo(board, "O")
        if checkWin(board):
            flag = "O"
            break

    if flag == "-":
        print("Remiza")

    elif flag == "X":
        print("X vyhral")

    elif flag == "O":
        print("O vyhral")


run = True
printBoard(board)

while run:

    flag = "-"
    printBoard(board)

    while checkWin(board) == 0 and checkTie(board) == 0:

        moveTo(board, "X")
        if checkWin(board):
            flag = "X"
            break

        if checkTie(board):
            break

        moveTo(board, "O")
        if checkWin(board):
            flag = "O"
            break

        printBoard(board)

    if flag == "-":
        print("Remiza")

    elif flag == "X":
        print("X vyhral")

    elif flag == "O":
        print("O vyhral")
