import os
import sys
import random
import time
from time import sleep

#VARIABLES

board = [
    ["B", ".", ".", "H", ".",".", ".", "R", ".", "."],
    ["🖑", ".", ".", ".", ".",".", ".", ".", ".", "."],
    [".", ".", ".", ".", "F",".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".",".", ".", ".", ".", "."],
    [".", "S", ".", ".", ".",".", "D", ".", ".", "E"]
]

player_fatigue = 0

#TEXT FILE READING

with open("player_enemy.txt") as file:
    player_hp, player_attack, enemy_hp, enemy_attack = [int(x) for x in file.read().split()]

with open("player_enemy.txt", "w") as file:
    file.write(f"{player_hp} {player_attack} {enemy_hp} {enemy_attack}")

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
def pull_out_sword():
        skill_check = random.randint(1, 20)
        if skill_check >= 15:
            print("You successfully pulled the sword out of the stone!")
            player_inventory.append("Not_a_zelda_ripoff")
            board[player_x][player_y] = "."
        else:
            print("You failed to pull the sword out of the stone. Keep trying.")

def bar():
    global player_gold
    global player_fatigue
    with open("player_gold.txt", "r") as file:
        player_gold = int(file.read())
    if player_fatigue >= 100:
        print("You are too tired to work, go home and sleep.")
    else:
        print("Welcome to the bar, you can work here and earn gold.")
        hours_worked = int(input("How many hours would you like to work? "))
        if hours_worked > 8:
            print("You can only work for 8 hours at a time.")
            hours_worked = 8
        earned_gold = hours_worked * random.randint(10, 20)
        player_gold += earned_gold
        player_fatigue += hours_worked * 10
        print(f"You earned {earned_gold} gold and your fatigue is now at {player_fatigue}.")
        with open("player_gold.txt", "w") as file:
            file.write(str(player_gold))

        drink = input("Would you like to get a drink? On the house")
        if drink == "yes":
            print("Here you go!")
            player_inventory.append("Drink")
        elif drink == "no":
            print("Alright buddy, suit yourself!")
        else:
            print("Is that a yes or a no?")

def rest_At_Home():
    global player_fatigue
    if player_fatigue > 80:
        print("Welcome home, time to sleep.")
        player_fatigue = 0
        print("You feel refreshed and your fatigue is now at 0.")
    else:
        print("The entity living under the bed demands a sacrafice, it is unsafe to sleep for now.")

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
        words = "Ok so I was working at my regular day job, an underpaid bar man at the tavern, when suddenly there were an influx of dwarves! I thought this was strange because they usually spend all year round up in the mines, so I had asked them! And they told me that there was a dragon in the caves where they had been mining, meaning that they couldn't work! The mining industry is the staple of this town, so please! Could you slay the dragon and free the mine? The town will forever be in your debt!"
        for char in words:
            sleep(0.05)
            sys.stdout.write(char)
    elif user_Input.lower() == 'no':
        print("Oh ok, it's alright. Come back later when you are ready to hear my story.")
    else:
        print('Type yes or no')

def interact_With_Dwarf():
    user_Input = input("Aye laddy! It be me! Yer old pal Groolgruth! Say you look flimsy! Tell you what! I'm thirsty, bring me a drink from the bar and I'll forge you up some armour! Whatda you say?\n")

    if user_Input.lower() == 'yes':
        if "Drink" in player_inventory:
            words = "Aye thank ye laddy! Let's forge up some of that armour now!"
            for char in words:
                sleep(0.05)
                sys.stdout.write(char)
            print("You got dwarf armour!")
            player_inventory.append("dwarf_armour")
    elif user_Input.lower() == 'no':
        print("Aye, it be ok. Come back later if you change your mind")
    else:
        print('That be a yes or a no?')

def interact_With_Fountain():
    user_Input = input("It's the town fountain, legend says if you put in 1 gold, you get good luck for 5 years. Do you want to put in 1 gold?\n")

    if user_Input.lower() == 'yes':
        print("You put in 1 gold")
        player_gold - 1
    elif user_Input.lower() == 'no':
        print("You don't put in 1 gold")
        input2 = input("But then you get an idea, other gullible idiots probably fell for this! What if you stole from the well?")
        if input2 == "yes":
            print("You reach your hand in and steal from the fountain!")
            player_gold + 50
        elif input2 == "no":
            print("Your right, it would be wrong for you to steal from the fountain")
        else:
            print("Yes or no")
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
                if "quality_sword" and "Not_a_zelda_ripoff" in player_inventory:
                    presses += 12
                elif "quality_sword" in player_inventory:
                    presses += 4
                elif "Not_a_zelda_ripoff" in player_inventory:
                    presses += 10
                else: 
                    presses += 2
        attack_power = player_attack + (presses * 0.1)
        enemy_hp -= attack_power
        if enemy_hp <= 0:
            board[enemy_x][enemy_y] = "."
            print("You defeated the enemy!")
            player_gold + 100
            break
        else:
            if "quality_armour" and "dwarf_armour" in player_inventory:
                player_hp -= enemy_attack-25
            elif "quality_armour" in player_inventory:
                player_hp -= enemy_attack-10
            elif "dwarf_armour" in player_inventory:
                player_hp -= enemy_attack-20
            else:
                player_hp -= enemy_attack
            print("Enemy attacked you for", enemy_attack, "damage!")
    if player_hp <= 0:
        print("You were defeated by the dragon.")
        print("Come back later when you are stronger...")
    return player_hp, enemy_hp

symbol_map = {
    "🖑": interact_With_Tutorial,
    "E": interact_With_Enemy,
    "S": shop,
    "F": interact_With_Fountain,
    "B": bar,
    "H": rest_At_Home,
    "R": pull_out_sword,
    "D": interact_With_Dwarf
}


#MAIN LOOP

while True:
    os.system('cls')
    print("Gold : ", player_gold)
    new_board = []
    for i in range(len(board)):
        new_board.append([])
        for j in range(len(board[0])):
            if i == player_x and j == player_y:
                new_board[i].append("@")
                symbol_map.get(board[i][j], lambda: None)()
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