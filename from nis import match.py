import os


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
    os.system('cls')
    for row in board:
        print(" ".join(row))
    print("Enter a direction to move (WASD):")
    direction = input()
    match direction:
        case 'w':
            if player_x > 0:
                board[player_x][player_y] = "."
                player_x -= 1
                board[player_x][player_y] = "@"
        case "a":
            if player_y > 0:
                board[player_x][player_y] = "."
                player_y -= 1
                board[player_x][player_y] = "@"
        case "s":
            if player_x < len(board) - 1:
                board[player_x][player_y] = "."
                player_x += 1
                board[player_x][player_y] = "@"
        case "d":
            if player_y < len(board[0]) - 1:
                board[player_x][player_y] = "."
                player_y += 1
                board[player_x][player_y] = "@"
        case default:
            print("WASD!")