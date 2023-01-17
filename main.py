import os
import sys
import random
import time
from time import sleep

#VARIABLES

board = [
    [".", ".", ".", ".", ".",".", ".", ".", ".", "."],
    ["🖑", ".", ".", ".", ".",".", ".", ".", ".", "."],
    [".", ".", ".", ".", "E",".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".",".", ".", ".", ".", "."],
    [".", "S", ".", ".", ".",".", ".", ".", ".", "."]
]


#TEXT FILE READING

with open("player_enemy.txt") as file:
    player_hp, player_attack, enemy_hp, enemy_attack = [int(x) for x in file.read().split()]

with open("player_enemy.txt", "w") as file:
    file.write(f"{player_hp} {player_attack} {100} {enemy_attack}")

def read_shop_items():
    with open("shop_items.txt", "r") as file:
        
        items = file.read()
    return items

with open("player_gold.txt", "r+") as file:
    player_gold = int(file.read())

#VARIABLES PT2

player_x, player_y = 1, 1

npc_x = 3
npc_y = 3
player_inventory = []

#FUNCTIONS

def shop():
    global player_gold
    items = {}
    with open("shop_inventory.txt") as file:
        for line in file:
            item, price = line.strip().split()
            items[item] = int(price)

    print("Welcome to the shop")
    print("Here is a list of items:")
    for item, price in items.items():
        print(f"{item}: {price} gold")

    while True:
        choice = input("Which item would you like to buy? (Enter 'exit' to leave the shop) ")
        if choice == "exit":
            break
        elif choice in items:
            if player_gold >= items[choice]:
                player_gold -= items[choice]
                player_inventory.append(choice)
                with open("player_gold.txt", "r+") as file:
                    file.write(str(player_gold))
                print("You bought the", choice + ".")
                print("You have", player_gold, "gold left.")
                print("You now have in inventory:", player_inventory)
                
            else:
                print("You don't have enough gold to buy that.")
        else:
            print("Invalid choice.")

def interact_With_Tutorial():
    user_Input = input("Hey! Do you want to hear my story? It's very interesting, and you might get something out of it.\n")

    if user_Input.lower() == 'yes':
        words = "Cant be asked to write this yet, come back later when I have finished writing"
        for char in words:
            sleep(0.05)
            sys.stdout.write(char)
    elif user_Input.lower() == 'no':
        print("Oh ok, it's alright. Come back later when you are ready to hear my story.")
    else:
        print('Type yes or no')

def interact_With_Enemy(player_hp, player_attack, enemy_hp, enemy_attack):
    while player_hp > 0 and enemy_hp > 0:
        print("Hey! I'm evil, so I'm gonna pwn you!")
        start_time = time.time()
        presses = 0
        while time.time() - start_time < 3:
            os.system('cls')
            print("Player HP:", player_hp)
            print("Enemy HP:", enemy_hp)
            print("Press the buttons that appear on screen to do damage")
            random_button = random.choice(['f', 'g', 'j', 'k'])
            print(random_button)
            player_input = input()
            if player_input in ['f', 'g', 'j', 'k'] and player_input == random_button:
                if "quality_sword" in player_inventory:
                    presses += 4
                else: 
                    presses += 2
        attack_power = player_attack + (presses * 0.1)
        enemy_hp -= attack_power
        if enemy_hp <= 0:
            print("You defeated the enemy!")
            player_gold + 100
            break
        else:
            player_hp -= enemy_attack
            print("Enemy attacked you for", enemy_attack, "damage!")
    if player_hp <= 0:
        print("You were defeated.")
    return player_hp, enemy_hp

#MAIN LOOP

while True:
    os.system('cls')
    print("Gold : ", player_gold)
    new_board = []
    for i in range(len(board)):
        new_board.append([])
        for j in range(len(board[0])):
            if i == player_x and j == player_y:
                if board[i][j] == "🖑":
                    new_board[i].append("@")
                    interact_With_Tutorial()
                elif board[i][j] == "E":
                    new_board[i].append("@")
                    player_hp, enemy_hp = interact_With_Enemy(player_hp, player_attack, enemy_hp, enemy_attack)
                elif board[i][j] == "S":
                    new_board[i].append("@")
                    shop()
                else:
                    new_board[i].append("@")
            else:
                new_board[i].append(board[i][j])
    for row in new_board:
        print(" ".join(row))
    direction = input("Enter a direction to move (WASD): ")
    if direction == 'w':
        if player_x > 0:
                player_x -= 1

    elif direction == "a":
        if player_y > 0:
            player_y -= 1
                
    elif direction == "s":
        if player_x < len(board) - 1:
            player_x += 1
                
    elif direction == "d":
        if player_y < len(board[0]) - 1:
            player_y += 1
    else:
        print("WASD!")
        