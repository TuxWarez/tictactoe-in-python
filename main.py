import random
arr = [["." for j in range(3)] for i in range(3)]
x = 0
char = 0
allowed = ['1', '2', '3']
list1 = [0, 1, 2]

def playermove():
    global xp
    global yp
    y = input("insert a character in xcoord,ycoord format: ")
    if len(y) > 3:
        print("The length of input is too long; try again")
        playermove()
    if "," not in y:
        print("The format in input is wrong; try again")
        playermove()
    if y[0] not in allowed or y[2] not in allowed:
        print("The numbers are out of range; try again")
        playermove()
    y = [int(i) - 1 for i in y.split(',')]
    if arr[y[0]][y[1]] == 'X' or arr[y[0]][y[1]] == 'O':
        print("There's already a character there; try again")
        playermove()
    xp, yp = y[0], y[1]
    return xp, yp

def cpumovebest(markmove):
    global row
    global col
    for row in range(3):
        for col in range(3):
            if arr[row][col] == '.':
                arr[row][col] = markmove
                if check(markmove):
                    arr[row][col] = '.'
                    return row, col
                arr[row][col] = '.'
    return None

def cpumoverandom():
    global xcord
    global ycord
    xcord = random.choice(list1)
    ycord = random.choice(list1)
    if arr[xcord][ycord] == 'X' or arr[xcord][ycord] == 'O':
        cpumoverandom()
    return xcord, ycord

def cpumove():
    move = cpumovebest(cpuchar)
    if move is not None:
        arr[row][col] = cpuchar
        return arr
    move = cpumovebest(char)
    print(move, row, col)
    if move is not None:
        arr[row][col] = cpuchar
        return arr
    cpumoverandom()
    arr[xcord][ycord] = cpuchar

def prtable():
    for i in arr:
        for j in i:
            print(f"{j}", end=' ')
        print()

def check(mark):
    if (arr[0][0] == mark and arr[1][1] == mark and arr[2][2] == mark) or (arr[0][2] == mark and arr[1][1] == mark and arr[2][0] == mark):
        return True
    for i in range(3):
        if arr[i][0] == mark and arr[i][1] == mark and arr[i][2] == mark:
            return True
    for i in range(3):
        if arr[0][i] == mark and arr[1][i] == mark and arr[2][i] == mark:
            return True
    return False

def choose():
    global char
    print("choose a character: ", end='')
    char = input()
    if char == 'x' or char == 'o':
        return char
    else:
        print('Try again;')
        choose()
choose()

def main():
    global char
    global x
    global cpuchar
    if char == 'x':
        cpuchar = 'O'
        char = 'X'
        playermove()
        arr[xp][yp] = char
        x = x + 1
        if x == 5:
            return
        if check(cpuchar):
            prtable()
            return
        char = 'O'
        cpumove()
        prtable()
        if check(cpuchar):
            return
        char = 'x'
        main()
    elif char == 'o':
        print(x)
        cpuchar = 'X'
        char = 'X'
        cpumove()
        prtable()
        if check(cpuchar):
            return
        char = 'O'
        playermove()
        arr[xp][yp] = char
        x = x + 1
        if x == 5:
            return
        if check(char):
            prtable()
            return
        char = 'o'
        main()
main()

if char == 'X' and flag == True:
    print("X won!")
elif char == 'O' and flag == True:
    print("O won!")
if not flag:
    print("Draw :(")

replay = input("Do you want to play another game? [y/N] ")

if replay == 'y':
    flag = False
    x = 0
    arr = [["." for j in range(3)] for i in range(3)]
    choose()
    main()
