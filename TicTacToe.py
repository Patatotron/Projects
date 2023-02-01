player = "z"
cell1 = ("#")
cell2 = ("#")
cell3 = ("#")
cell4 = ("#")
cell5 = ("#")
cell6 = ("#")
cell7 = ("#")
cell8 = ("#")
cell9 = ("#")
win = 0
turn = 1
for turn in range(1,10):
    import os
    os.system('clear')
    if win == 1:
        print("The winner is 'X'")
        break
    elif win == 2:
        print("The winner is 'O'")
        break
    else:
        if turn % 2 == 1:
            player = "X"
        else:
            player = "O"
        print()
        print()
        print(cell1,cell2,cell3)
        print(cell4,cell5,cell6)
        print(cell7,cell8,cell9)

        print()
        print()

        input2 = int(input("Enter the number of the cell where you want to place your sign (player:%s):" % player))

        if input2 == 1:
            if turn % 2 == 1:
                if cell1 == ("#"):
                    cell1 = ("X")
            elif cell1 == ("#"):
                    cell1 = ("O")
        if input2 == 2:
            if turn % 2 == 1:
                if cell2 == ("#"):
                    cell2 = ("X")
            elif cell2 == ("#"):
                cell2 = ("O")
        if input2 == 3:
            if turn % 2 == 1:
                if cell3 == ("#"):
                    cell3 = ("X")
            elif cell3 == ("#"):
                    cell3 = ("O")
        if input2 == 4:
            if turn % 2 == 1:
                if cell4 == ("#"):
                    cell4 = ("X")
            elif cell4 == ("#"):
                    cell4 = ("O")
        if input2 == 5:
            if turn % 2 == 1:
                if cell5 == ("#"):
                    cell5 = ("X")
            elif cell5 == ("#"):
                    cell5 = ("O")
        if input2 == 6:
            if turn % 2 == 1:
                if cell6 == ("#"):
                    cell6 = ("X")
            elif cell6 == ("#"):
                    cell6 = ("O")
        if input2 == 7:
            if turn % 2 == 1:
                if cell7 == ("#"):
                    cell7 = ("X")
            elif cell7 == ("#"):
                    cell7 = ("O")
        if input2 == 8:
            if turn % 2 == 1:
                if cell8 == ("#"):
                    cell8 = ("X")
            elif cell8 == ("#"):
                    cell8 = ("O")
        if input2 == 9:
            if turn % 2 == 1:
                if cell9 == ("#"):
                    cell9 = ("X")
            elif cell9 == ("#"):
                    cell9 = ("O")
        if cell1 == ("X"):
            if cell2 == ("X"):
                if cell3 == ("X"):
                    win = 1
        if cell4 == ("X"):
            if cell5 == ("X"):
                if cell6 == ("X"): 
                    win = 1
        if cell7 == ("X"):
            if cell8 == ("X"):
                if cell9 == ("X"):
                    win = 1
        if cell1 == ("O"):
            if cell2 == ("O"):
                if cell3 == ("O"):
                    win = 2
        if cell4 == ("O"):
            if cell5 == ("O"):
                if cell6 == ("O"): 
                    win = 2
        if cell7 == ("O"):
            if cell8 == ("O"):
                if cell9 == ("O"):
                    win = 2
        if cell1 == ("X"):
            if cell4 == ("X"):
                if cell7 == ("X"):
                    win = 1
        if cell2 == ("X"):
            if cell5 == ("X"):
                if cell8 == ("X"):
                    win = 1
        if cell3 == ("X"):
            if cell6 == ("X"):
                if cell9 == ("X"):
                    win = 1
        if cell1 == ("O"):
            if cell4 == ("O"):
                if cell7 == ("O"):
                    win = 2
        if cell2 == ("O"):
            if cell5 == ("O"):
                if cell8 == ("O"):
                    win = 2
        if cell3 == ("O"):
            if cell6 == ("O"):
                if cell9 == ("O"):
                    win = 2
        if cell1 == ("X"):
            if cell5 == ("X"):
                if cell9 == ("X"):
                    win = 1
        if cell3 == ("X"):
            if cell5 == ("X"):
                if cell7 == ("X"):
                    win = 1
        if cell1 == ("O"):
            if cell5 == ("O"):
                if cell9 == ("O"):
                    win = 2
        if cell3 == ("O"):
            if cell5 == ("O"):
                if cell7 == ("O"):
                    win = 2

if win == 0:
    print()
    print()
    print(cell1,cell2,cell3)
    print(cell4,cell5,cell6)
    print(cell7,cell8,cell9)
    print("The game is a draw")
else :
    print("Game Over")
