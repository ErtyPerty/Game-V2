import os
import sys
import random
from time import sleep

board = [
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."]
]

player_x, player_y = 2, 2
board[player_x][player_y] = "@"

while True:
    for row in board:
        print(" ".join(row))
    print("Enter a direction to move (WASD):")
    direction = input()
    switch = {
        "w": lambda: (player_x > 0) and (player_x-1, player_y),
        "a": lambda: (player_y > 0) and (player_x, player_y-1),
        "s": lambda: (player_x < len(board)-1) and (player_x+1, player_y),
        "d": lambda: (player_y < len(board[0])-1) and (player_x, player_y+1)
    }
    new_x, new_y = switch.get(direction, lambda: (player_x, player_y))()
    board[player_x][player_y] = "."
    player_x, player_y = new_x, new_y
    board[player_x][player_y] = "@"