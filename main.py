import os
import random
import time


player_data = open("player.txt","r+")

content = player_data.readlines()


grid = [['.', '.', '.'],
        ['.', '.', '.'],
        ['❑', '.', '.']]

player_x = 1
player_y = 1

player_inventory = {}


def print_grid():
    for row in range(len(grid)):
        for cell in range(len(grid[0])):
            if row == player_y and cell == player_x:
                print('⇩', end=' ')
            else:
                print(grid[row][cell], end=' ')
        print()
    print()
    print("Gold : ")
    print(content[0])


print_grid()

shop_inventory = {'sword': 50, 'armour': 100}

def enter_shop():
    global player_inventory
    print("Welcome to the shop!")
    print("Inventory:")
    for item, price in shop_inventory.items():
        print(f"{item}: {price} gold")
    while True:
        item = input("What would you like to buy? (type 'exit' to leave the shop)")
        if item in shop_inventory:
            match item:
                case 


#Main loop
while True:
    move = input("Move (WASD): ")
    if move.upper() == 'W':
        if player_y > 0:
            player_y -= 1
    elif move.upper() == 'A':
        if player_x > 0:
            player_x -= 1
    elif move.upper() == 'S':
        if player_y < len(grid) - 1:
            player_y += 1
    elif move.upper() == 'D':
        if player_x < len(grid[0]) - 1:
            player_x += 1

  
  #Position checks
    if grid[player_y][player_x] == '❑':
        enter_shop()

  

    os.system('cls')
    print_grid()
    