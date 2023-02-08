import os
import sys, time 

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
        break
    else:
        break



while turn <= 9 or winnerO == False or winnerX == False:
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
                break
            elif winnerX == True:
                os.system('clear')
                break

            else:
                turn += 1
                continue

if winnerO == True:
    printBoard()
    print("The winner is O")
elif winnerX == True:
    printBoard()
    print("The winner is X")