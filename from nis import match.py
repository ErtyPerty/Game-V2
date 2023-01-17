import os
import sys
import random
import time
from time import sleep

board = [
    [".", ".", ".", ".", ".",".", ".", ".", ".", "."],
    ["🖑", ".", ".", ".", ".",".", ".", ".", ".", "."],
    [".", ".", ".", ".", "E",".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".",".", ".", ".", ".", "."],
    [".", "S", ".", ".", ".",".", ".", ".", ".", "."]
]

player_x, player_y = 1, 1

npc_x = 3
npc_y = 3


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
                presses += 2
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
    return player_hp, enemy_hp



with open("player_enemy.txt") as file:
    player_hp, player_attack, enemy_hp, enemy_attack = [int(x) for x in file.read().split()]



with open("player_enemy.txt", "w") as file:
    file.write(f"{player_hp} {player_attack} {100} {enemy_attack}")



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


while True:
    os.system('cls')
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
        
