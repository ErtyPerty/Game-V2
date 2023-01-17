from nis import match
import os
import sys
import random
from time import sleep

grid = [['.' for x in range(4)] for y in range(4)]
player_icon = "P"

def move_player(x, y):
    # Check if the new position is within the grid boundaries
    if x < 0 or x > 3 or y < 0 or y > 3:
        print("Invalid")
    else:
        # Move the player to the new position
        grid[x][y] = player_icon
        print_grid()

def print_grid():
    for row in grid:
        print(" ".join(row))

# Initial position of the player
player_x = 0
player_y = 0
grid[player_x][player_y] = player_icon

print_grid()

while True:
    direction = input("Move around the map with WASD: ")
    match direction:
        case 'w':
            grid[player_x][player_y] = '.'
            move_player(player_x - 1, player_y)
        case 'a':
            grid[player_x][player_y] = '.'
            move_player(player_x, player_y - 1)     
        case 's':
            grid[player_x][player_y] = '.'
            move_player(player_x + 1, player_y)
        case 'd':
            grid[player_x][player_y] = '.'
            move_player(player_x, player_y + 1)