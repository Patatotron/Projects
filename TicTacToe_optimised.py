import os
import sys, time 
import random

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
winnerX = False
winnerO = False
wrongInput = False
Green = "\u001b"
tutorial = "This is how you need to place your signs"
text_speed = 0.08
turn = 0
z = 0

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
    for y in range(0,9,3):
        if board[y] == "X":
            if board[y+1] == "X":
                if board[y+2] == "X":
                    winnerX = True
        elif board[y] == "O":
            if board[y+1] == "O":
                if board[y+2] == "O":
                    winnerO = True

def CheckCol():
    global board
    global winnerX
    global winnerO
    for y in range(0,3):
        if board[y] == "X":
            if board[y+3] == "X":
                if board[y+6] == "X":
                    winnerX = True
        else:
            if board[y] == "O":
                if board[y+3] == "O":
                    if board[y+6] == "O":
                        winnerO = True


def CheckDiag():
    global board
    global winnerX
    global winnerO
    if board[0] == board[4] and board[4] == board[8] and board[0] == "X":
        winnerX = True
    elif board[0] == board[4] and board[4] == board[8] and board[0] == "O":
        winnerO = True
    elif board[2] == board[4] and board[4] == board[6] and board[2] == "X":
        winnerX = True
    elif board[2] == board[4] and board[4] == board[6] and board[2] == "O":
        winnerO = True

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
    os.system('clear')
    printBoard()
    player_input = int(input("Enter sign location:")) - 1
    PlaceSign()
    if wrongInput == True:
        print("Wrong input, please try again")
        wrongInput = False
        continue
    else:
        CheckWinner()
        if winnerO == True:
            print("The winner is O!")
            break
        elif winnerX == True:
            print("The winner is X!")
        else:
            turn += 1
            continue