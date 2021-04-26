import os
from time import sleep

grid = [
["-", "-", "-"],
["-", "-", "-"],
["-", "-", "-"],
]

valid_numbers = ["1", "2", "3"]

def reset_board():
    grid = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"],
    ]

def print_grid():
    os.system("CLS")
    for i in range(1, 4):
        print(i, end=" | ")
        for j in range(1, 4):
            print(grid[i-1][j-1], end='   ')
        print()
    print("    1   2   3")

def check_input(place):
    if("," not in place):
        return False
    positions = place.split(",")
    if(positions[0] not in valid_numbers) or (positions[1] not in valid_numbers):
        return False
    else:
        if(grid[int(positions[1])-1][int(positions[0])-1] == "-"):
            return True
        else:
            return False

def change_turn(turn):
    if(turn == "X"):
        return "O"
    else:
        return "X"

def place_piece(tile, place):
    x = int(place[0])-1
    y = int(place[2])-1
    grid[y][x] = tile

def check_for_winner(turn):
    for a in range(0, 3): # Checking rows and columns
        if(grid[a][0] == grid[a][1] == grid[a][2] == turn):
            return "Player " + turn + " wins"
    for b in range(0, 3):
        if(grid[0][b] == grid[1][b] == grid[2][b] == turn):
            return "Player " + turn + " wins"
    if((grid[0][0] == grid[1][1] == grid[2][2] == turn) or (grid[2][0] == grid[1][1] == grid[0][2]) == turn):
        return "Player " + turn + " wins"
    return False

def game():
    while(1):
        reset_board()
        turn = "X"
        winner = False
        while(winner == False):
            print_grid()
            print("It is player: " + turn + "'s turn.")
            place = input("Enter where you would like to put your piece (wrriten as x,y):\n")
            valid = check_input(place)
            while(valid == False):
                print("Invalid input, please try again :)")
                place = input()
                valid = check_input(place)
            place_piece(turn, place)
            winner = check_for_winner(turn)
            turn = change_turn(turn)
        reset_board()
        print_grid()
        print(winner)
        print("Will restart soon.")
        sleep(5)
        turn = "X"

game()
