import random
import os

grid = [["." for j in range(3)] for i in range(3)]
game_over = False
x = 0
char = 0
allowed = ['1', '2', '3']
game_over_1 = False

def player_move():
    xy = input("insert a character in xcoord,ycoord format: ")
    if len(xy) > 3:
        print("The length of input is too long; try again")
        player_move()
    if "," not in xy:
        print("The format in input is wrong; try again")
        player_move()
    if xy[0] not in allowed or xy[2] not in allowed:
        print("The numbers are out of range; try again")
        player_move()
    xy = [int(i) - 1 for i in xy.split(',')]
    if grid[xy[0]][xy[1]] == 'X' or grid[xy[0]][xy[1]] == 'O':
        print("There's already a character there; try again")
        player_move()
    grid[xy[0]][xy[1]] = char

def cpu_move_best(markmove):
    global row
    global col
    for row in range(3):
        for col in range(3):
            if grid[row][col] == '.':
                grid[row][col] = markmove
                if check(markmove):
                    grid[row][col] = '.'
                    return row, col
                grid[row][col] = '.'
    return None

def cpu_move_random():
    xcord = random.randint(0, 2)
    ycord = random.randint(0, 2)
    if grid[xcord][ycord] == 'X' or grid[xcord][ycord] == 'O':
        cpu_move_random()
    grid[xcord][ycord] = cpuchar

def cpu_move():
    move = cpu_move_best(cpuchar)
    if move is not None:
        grid[row][col] = cpuchar
        return grid
    move = cpu_move_best(char)
    if move is not None:
        grid[row][col] = cpuchar
        return grid
    cpu_move_random()

def print_table():
    for i in grid:
        for j in i:
            print(f"{j}", end=' ')
        print()

def check(mark):
    if (grid[0][0] == mark and grid[1][1] == mark and grid[2][2] == mark) or (grid[0][2] == mark and grid[1][1] == mark and grid[2][0] == mark):
        return True
    for i in range(3):
        if grid[i][0] == mark and grid[i][1] == mark and grid[i][2] == mark:
            return True
    for i in range(3):
        if grid[0][i] == mark and grid[1][i] == mark and grid[2][i] == mark:
            return True
    return False

def choose():
    global char
    print("choose a character: ", end='')
    char = input()
    if char == 'x' or char == 'o':
        return char
    print('Try again;')
    choose()

def play_turn():
    global char
    global x
    global cpuchar
    global game_over
    if char == 'x':
        char = 'X'
        player_move()
        game_over = check(char)
        x = x + 1
        if x == 5:
            return True
        if game_over == True:
            os.system('clear')
            print_table()
            return True
        cpuchar = 'O'
        char = 'O'
        cpu_move()
        os.system('clear')
        print_table()
        game_over = check(cpuchar)
        if game_over == True:
            return True
        char = 'x'
    elif char == 'o':
        cpuchar = 'X'
        char = 'X'
        cpu_move()
        os.system('clear')
        print_table()
        game_over = check(cpuchar)
        if game_over == True:
            return True
        char = 'O'
        player_move()
        game_over = check(char)
        x = x + 1
        if x == 5:
            return True
        if game_over == True:
            os.system('clear')
            print_table()
            return True
        char = 'o'

def print_result():
    if game_over:
        print(f'{char} won!')
        return
    print("Draw :(")

def play_game():
    global grid
    global x
    choose()
    x = 0
    grid = [["." for j in range(3)] for i in range(3)]
    while True:
        game_over_1 = play_turn()
        if game_over_1:
            return

while True:
    play_game()
    print_result()
    if input("Do you want to play another game? [y/N] ")!="y":
        break
