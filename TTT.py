import os
import sys, time
import random

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
winnerX = False
winnerO = False
wrongInput = False
Green = "\u001b[32m"
white = "\u001b[37m"
tutorial = (Green + "This is how you need to place your signs" + white)
text_speed = 0.08
turn = 0
z = 0
red = "\u001b[31m"
empty = False
possible_moves = []
player = ""

def PlaceSign():
    global board
    global player_input
    global wrongInput
    if board[player_input] == " ":
        if turn % 2 == 0:
            board[player_input] = "X"
        else:
            board[player_input] = "O"
    else:
        wrongInput = True

def PlaceSignAi():
    global board
    global player_input
    global wrongInput
    if board[player_input] == " ":
        board[player_input] = "X"
    else:
        wrongInput = True

def printBoard():
    global board
    print()
    print("     |     |     ")
    print("  "+board[0]+"  |  "+board[1]+"  |  "+board[2]+"  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print("  "+board[3]+"  |  "+board[4]+"  |  "+board[5]+"  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print("  "+board[6]+"  |  "+board[7]+"  |  "+board[8]+"  ")
    print("     |     |     ")
    print()

def printExample():
    global board
    print()
    print("     |     |     ")
    print("  ""1""  |  ""2""  |  ""3""  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print("  ""4""  |  ""5""  |  ""6""  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print("  ""7""  |  ""8""  |  ""9""  ")
    print("     |     |     ")
    print()


def CheckRow():
    global board
    global winnerX
    global winnerO
    global red
    global white
    for y in range(0,9,3):
        if board[y] == "X":
            if board[y+1] == "X":
                if board[y+2] == "X":
                    winnerX = True
                    board[y] = (red + "X" + white)
                    board[y+1] = (red + "X" + white)
                    board[y+2] = (red + "X" + white)
        elif board[y] == "O":
            if board[y+1] == "O":
                if board[y+2] == "O":
                    winnerO = True
                    board[y] = (red + "O" + white)
                    board[y+1] = (red + "O" + white)
                    board[y+2] = (red + "O" + white)

def CheckCol():
    global board
    global winnerX
    global winnerO
    global red
    global white
    for y in range(0,3):
        if board[y] == "X":
            if board[y+3] == "X":
                if board[y+6] == "X":
                    winnerX = True
                    board[y] = (red + "X" + white)
                    board[y+3] = (red + "X" + white)
                    board[y+6] = (red + "X" + white)
        else:
            if board[y] == "O":
                if board[y+3] == "O":
                    if board[y+6] == "O":
                        winnerO = True
                        board[y] = (red + "O" + white)
                        board[y+3] = (red + "O" + white)
                        board[y+6] = (red + "O" + white)

def EmptyBoard():
    global board
    global empty
    if board.count(" ") == 0:
        empty = True
    else:
        empty = False

def CheckDiag():
    global board
    global winnerX
    global winnerO
    global red
    global white
    if board[0] == board[4] and board[4] == board[8] and board[0] == "X":
        winnerX = True
        board[0] = (red + "X" + white)
        board[4] = (red + "X" + white)
        board[8] = (red + "X" + white)
    elif board[0] == board[4] and board[4] == board[8] and board[0] == "O":
        winnerO = True
        board[0] = (red + "O" + white)
        board[4] = (red + "O" + white)
        board[8] = (red + "O" + white)
    elif board[2] == board[4] and board[4] == board[6] and board[2] == "X":
        winnerX = True
        board[2] = (red + "X" + white)
        board[4] = (red + "X" + white)
        board[6] = (red + "X" + white)
    elif board[2] == board[4] and board[4] == board[6] and board[2] == "O":
        winnerO = True
        board[2] = (red + "O" + white)
        board[4] = (red + "O" + white)
        board[6] = (red + "O" + white)

def CheckWinner():
    CheckCol()
    CheckDiag()
    CheckRow()

def PVP():
    global board
    global player_input
    global wrongInput
    global winnerO
    global winnerX
    global turn
    global white
    global red
    global Green
    global z
    global tutorial
    global text_speed
    global empty
    global player
    while z == 0:
        os.system('clear')
        y_n = str(input("Do you want the tutorial, (y) or (n):"))
        if y_n == "y":
            os.system('clear')
            printExample()
            for i in tutorial: 
                print(i, end='') 
                sys.stdout.flush() 
                time.sleep(text_speed)
            time.sleep(4)
            z += 1
        else:
            z += 1
    while z == 0:
            os.system('clear')
            y_n = str(input("Do you want the tutorial, (y) or (n):"))
            if y_n == "y":
                os.system('clear')
                printExample()
                for i in tutorial: 
                    print(i, end='') 
                    sys.stdout.flush() 
                    time.sleep(text_speed)
                time.sleep(4)
                z += 1
            else:
                z += 1
    while turn <= 9 or winnerO == False or winnerX == False:
        if " " in board:
            if turn % 2 == 0:
                player = "X"
            else:
                player = "O"

            os.system('clear')
            printBoard()
            try:
                player_input = int(input("Enter sign location (%s):" % player)) - 1
            except ValueError:
                print("Wrong input, please try again")
                time.sleep(2)
                continue

            try:
                PlaceSign()
            except IndexError:
                print("Wrong input, please try again")
                time.sleep(2)
                continue
            if wrongInput == True:
                    print("Wrong input, please try again")
                    time.sleep(2)
                    wrongInput = False
                    continue
            else:
                    CheckWinner()
                    if winnerO == True:
                        os.system('clear')
                        printBoard()
                        print("The winner is O")
                        sys.exit()
                    elif winnerX == True:
                        os.system('clear')
                        printBoard()
                        print("The winner is X")
                        sys.exit()
                    else:
                        turn += 1
                        continue
        else:
            os.system('clear')
            printBoard()
            print("The game is a draw")

def Validmoves():
    global board
    global possible_moves
    possible_moves = []
    for x in range(len(board)):
        if board[x] == " ":
            possible_moves.append(x)
    return possible_moves

def Minimax():
    global board
    global possible_moves
    global choose_move
    if " " in board:
        Validmoves()
        choose_move = random.choice(possible_moves)
        board[choose_move] = "O"
    else:
        sys.exit()


    
def PVAI():
    global board
    global player_input
    global wrongInput
    global winnerO
    global winnerX
    global turn
    global white
    global red
    global Green
    global z
    global tutorial
    global text_speed
    global empty
    while z == 0:
        os.system('clear')
        y_n = str(input("Do you want the tutorial, (y) or (n):"))
        if y_n == "y":
            os.system('clear')
            printExample()
            for i in tutorial: 
                print(i, end='') 
                sys.stdout.flush() 
                time.sleep(text_speed)
            time.sleep(4)
            z += 1
        else:
            break
    while turn <= 9 or winnerO == False or winnerX == False:
        if " " in board:
            os.system('clear')
            printBoard()
            player_input = int(input("Enter sign location:")) - 1
            if board[player_input] == " ":
                if wrongInput == True:
                    print("Wrong input, please try again")
                    time.sleep(2)
                    continue
                else:
                    PlaceSignAi()
                    CheckWinner()
                    if winnerO == True:
                        os.system('clear')
                        printBoard()
                        print("The winner is O")
                        sys.exit()

                    elif winnerX == True:
                        os.system('clear')
                        printBoard()
                        print("The winner is X")
                        sys.exit()
                    else:
                        Minimax()
                        CheckWinner()
                        if winnerO == True:
                            os.system('clear')
                            printBoard()
                            print("The winner is O")
                            sys.exit()
                        elif winnerX == True:
                            os.system('clear')
                            printBoard()
                            print("The winner is X")
                            sys.exit()
                        else:
                            turn += 1
                            continue
            else:
                print("Wrong input, please try again")
                time.sleep(2)
                continue
        else:
            os.system('clear')
            printBoard()
            print("The game is a draw")

while True:
    os.system('clear')
    k = str(input("Enter 1 to play against humain or 2 to play against AI:"))
    if k == "1":
        PVP()
    elif k == "2":
        PVAI()
    else:
        print("Please enter the number 1 or 2")
