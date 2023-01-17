import os
import sys
import random
import time
from time import sleep

board = [
    [".", ".", ".", ".", "."],
    ["🖑", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."]
]

player_x, player_y = 2, 2

npc_x = 3
npc_y = 3

with open("player_enemy.txt") as file:
    player_hp, player_attack, enemy_hp, enemy_attack = [int(x) for x in file.read().split()]

def interact_With_Enemy():
    while player_hp > 0 and enemy_hp > 0:
        print("Player HP:", player_hp)
        print("Enemy HP:", enemy_hp)
        print("Press the 'a' key as fast as you can for 3 seconds to attack the enemy!")
        start_time = time.time()
        presses = 0
        while time.time() - start_time < 3:
            if input() == "a":
                presses += 1
        attack_power = player_attack + (presses * 0.1)
        enemy_hp -= attack_power
        if enemy_hp <= 0:
            print("You defeated the enemy!")
            break
        else:
            player_hp -= enemy_attack
            print("Enemy attacked you for", enemy_attack, "damage!")

    if player_hp <= 0:
        print("You were defeated.")

# write player and enemy values to text file
with open("player_enemy.txt", "w") as file:
    file.write(f"{player_hp} {player_attack} {enemy_hp} {enemy_attack}")

def interact_With_Tutorial():
   #NPC Code
    user_Input = input("Hey! Do you want to hear my story? It's very interesting, and you might get something out of it.\n")

    if user_Input.lower() == 'yes':
        words = ""
        for char in words:
            sleep(0.05)
            sys.stdout.write(char)
    elif user_Input.lower() == 'no':
        print("Oh ok, it's alright. Come back later when you are ready to hear my story.")
    else:
        print('Type yes or no')


while True:
    os.system('cls')
    new_board = []
    for i in range(len(board)):
        new_board.append([])
        for j in range(len(board[0])):
            if i == player_x and j == player_y:
                if board[i][j] == "🖑":
                    new_board[i].append("@")
                    interact_with_tutorial()
                else:
                    new_board[i].append("@")
            else:
                new_board[i].append(board[i][j])
    for row in new_board:
        print(" ".join(row))
    print("Enter a direction to move (WASD):")
    direction = input()
    match direction:
        case 'w':
            if player_x > 0:
                player_x -= 1

        case "a":
            if player_y > 0:
                player_y -= 1
            
        case "s":
            if player_x < len(board) - 1:
                player_x += 1
             
        case "d":
            if player_y < len(board[0]) - 1:
                player_y += 1
           
        case default:
            print("WASD!")
        
