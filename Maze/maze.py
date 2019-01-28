import sys



grid = [["b",".","s","w"], [".","w","w","s"]]

x = 0
y = 0


def canIgo(pos):
    if wall(pos) == False and pos == "." or pos == "s":
        return True
    return False


def wall(pos):
    if pos == "w":
        return True
    return False


def moveUp():

    global x
    xPrev = x
    x = x - 1
    symbol = grid[x][y]
    if canIgo(symbol) == True:
        if grid[x][y] == "s":
            printGrid()
            sys.exit("Finished!")
        else:
            grid[xPrev][y] = "."
            grid[x][y] = "b"
            printGrid()
    else:
        x = xPrev
        print("Cant go! \n")
        printGrid()



def moveDown():

    global x
    xPrev = x
    x = x + 1
    symbol = grid[x][y]
    if canIgo(symbol) == True:
        if grid[x][y] == "s":
            printGrid()
            sys.exit("Finished!")
        else:
            grid[xPrev][y] = "."
            grid[x][y] = "b"
            printGrid()
    else:
        x = xPrev
        print("Cant go! \n")
        printGrid()
            
    

def moveRight():
    
    global y 
    yPrev = y
    y = y + 1
    symbol = grid[x][y]
    if canIgo(symbol) == True:
        if grid[x][y] == "s":
            printGrid()
            sys.exit("Finished")
        else:
            grid[x][yPrev] = "."
            grid[x][y] = "b"
            printGrid()
    else:
        y = yPrev
        print("Cant go! \n")
        printGrid()

def moveLeft():

    global y
    yPrev = y
    y = y - 1
    symbol = grid[x][y]
    if canIgo(symbol) == True:
        if grid[x][y] == "s":
            printGrid()
            sys.exit("Finished!")
        else:
            grid[x][yPrev] = "."
            grid[x][y] = "b"
            printGrid()
    else:
        y = yPrev
        print("Cant go! \n")
        printGrid()

    


def inputGame(symb):
    #move up
    if symb == "u":
        return moveUp()
    #move down
    elif symb == "d":
        return moveDown()
    #move right
    elif symb == "r":
        return moveRight()
    #move left
    elif symb == "l":
        return moveLeft()


def printGrid():
    print("GRID:")
    for i in range(2):
        print("\n")
        for j in range(4):
            print(grid[i][j], end =" ")
    print("\n")


def menu():
    print("Choose what u want!\n")
    print("1 - Play")
    print("2 - Exit")
    choice = input()
    if choice == "1":
        printGrid()
        symbol = input()
        while symbol != "e":
            inputGame(symbol)
            symbol = input()
    else:
        sys.exit("U quit!")

menu()
        

            

    


    


