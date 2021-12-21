"""
Battleship Project
Name:
Roll No:
"""

import battleship_tests as test

project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *
import random

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4


'''
makeModel(data)
Parameters: dict mapping strs to values
Returns: None
'''

def makeModel(data):
    data["rows"] = 10
    data["cols"] = 10
    data["boardsize"] = 500
    data["cellsize"] = 50
    data["numShips"] = 5
    g = emptyGrid(data["rows"], data["cols"])
    data["userboard"] = g
    g1 = emptyGrid(data["rows"], data["cols"])
    k1 = addShips(g1, data["numShips"])
    data["computer board"] = k1
    data["temp_ship"] = []
    data["shipcount"] = 0

    return


'''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    grid1=data["userboard"]
    drawGrid(data, userCanvas, grid1,showShips=True)

    grid2=data["computer board"]
    drawGrid(data, compCanvas, grid2,showShips=True)
    drawShip(data,userCanvas,data["temp_ship"])
    return


'''
keyPressed(data, events)
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
    pass


'''
mousePressed(data, event, board)
Parameters: dict mapping strs to values ; mouse event object ; 2D list of ints
Returns: None
'''
def mousePressed(data, event, board):
    a = getClickedCell(data, event)
    # print(board)
    if board == "user":
        clickUserBoard(data, a[0], a[1])
        # data["temp_ship"].append(a)

    elif board == "comp":
        pass

#### WEEK 1 ####

'''
emptyGrid(rows, cols)
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols):
    a=[]
    b=[]
    for i in range(int(rows)):
        a = []
        for j in range(int(cols)):
            a.append(1)
        b.append(a)

    return b


'''
createShip()
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():
    row = random.randint(1,8)
    col = random.randint(1,8)
    #print(row,col)
    k= random.randint(0,1)
    #print (k)
    if k==0:
        ship=[[row-1,col],[row,col],[row+1,col]]
        #print (ship)
    elif k==1:
        ship=[[row,col-1],[row,col],[row,col+1]]
        #print(ship)
    return ship


'''
checkShip(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):
    h=0
    for i in range(len(ship)):
        a=ship[i]
        
        b=a[0]
        c=a[1]
        if grid[b][c]==1:
            h=h+1
    
    if h==len(ship):
        a1=True
    else:
        a1=False
        
    return a1

'''
addShips(grid, numShips)
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
def addShips(grid, numShips):
    count1=0
    while count1<numShips:
        #print(count1)
        ship=createShip()
        #print(ship)
        g=checkShip(grid,ship)
        #print(g)
        if g:
            for i in range(len(ship)):
                a1=ship[i]
                a=a1[0]
                b=a1[1]
                grid[a][b]=2

            count1=count1+1   
    return grid

'''
drawGrid(data, canvas, grid, showShips)
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips):
    cols = data["cols"]
    rows = data["rows"]
    cellsize = data["cellsize"]
    w = canvas
    st = []
    n = 0
    for i in range(rows + 1):
        st.append(n)
        n = n + cellsize

    for i in range(cols):
        for j in range(rows):
            if grid[i][j] == 1:
                w.create_rectangle(st[j], st[i], st[j + 1], st[i + 1], fill="blue", outline='black', width=2)
            elif grid[i][j] == 2:
                w.create_rectangle(st[j], st[i], st[j + 1], st[i + 1], fill="yellow", outline='black', width=2)
    
    
    
    return


### WEEK 2 ###

'''
isVertical(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):
    rowcord=[]
    colcord=[]
    for i in range(len(ship)):
        rowcord.append(ship[i][0])
    for j in range(len(ship)):
        colcord.append(ship[j][1])

    #print (rowcord,colcord)
    if colcord[0] == colcord[1] & colcord[1] == colcord[2]:
        a=True
    else:
        a=False
    rowcord.sort()
    p=rowcord[0]
    q=rowcord[1]
    r=rowcord[2]
    diff1=abs(r-q)
    diff2=abs(q-p)
    if diff1==1 & diff2==1:
        b=True
    else:
        b=False
    #print(b)
    if a==True & b==True:
            k=True

    else:
        k=False


    return k


'''
isHorizontal(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
    rowcord=[]
    colcord=[]
    for i in range(len(ship)):
        rowcord.append(ship[i][0])
    for j in range(len(ship)):
        colcord.append(ship[j][1])

    if rowcord[0] == rowcord[1] & rowcord[1] == rowcord[2]:
        a=True
    else:
        a=False

    colcord.sort()
    p=colcord[0]
    q=colcord[1]
    r=colcord[2]
    diff1=abs(r-q)
    diff2=abs(q-p)
    if diff1==1 & diff2==1:
        b=True
    else:
        b=False
    if a==True & b==True:
            k=True
    else:
        k=False
    return k


'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
    a=data["cellsize"]
    col=int(event.x/a)
    row=int(event.y/a)
    lst=[]
    lst.append(row)
    lst.append(col)
    return lst
    

'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    cols = data["cols"]
    rows = data["rows"]
    cellsize = data["cellsize"]
    for j in ship:
        a = j[1] * cellsize
        b = j[0] * cellsize
        canvas.create_rectangle(a, b, a + cellsize, b + cellsize, fill="white")
    return



'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
    if len(ship) == 3:
        a = checkShip(grid, ship)
        if a == True:
            if isVertical(ship) == True:
                b = True
            elif isHorizontal(ship) == True:
                b = True
            else:
                b = False
        else:
            b = False
    else:
        b = False
    if b == True:
        k = True
    else:
        k = False
    return k


'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):
    ship = data["temp_ship"]
    grid = data["userboard"]
    a = shipIsValid(grid, ship)
    if a == True:
        for i in range(len(ship)):
            a = ship[i][0]
            b = ship[i][1]
            grid[a][b] = 2
            data["userboard"] = grid
        data["shipcount"] = data["shipcount"] + 1
    elif a == False:
        print("Ship is not Valid")
    # print(data["userboard"])
    data["temp_ship"] = []
    return



'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    if data["shipcount"] < 5:
        ship = data["temp_ship"]
        cell = [row, col]
        if cell in ship:
            return None

        else:
            data["temp_ship"].append(cell)
            k = len(data["temp_ship"])

            if k == 3:
                placeShip(data)

    elif data["shipcount"] == 5:
        print("You can start the game")

    return



### WEEK 3 ###

'''
updateBoard(data, board, row, col, player)
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):
    return


'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col):
    return


'''
getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):
    return


'''
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    return


'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    return


### SIMULATION FRAMEWORK ###

from tkinter import *

def updateView(data, userCanvas, compCanvas):
    userCanvas.delete(ALL)
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)

def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    makeModel(data)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    # We need two canvases - one for the user, one for the computer
    Label(root, text = "USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text = "COMPUTER BOARD - click to make guesses. The computer will guess on your board.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()

    makeView(data, userCanvas, compCanvas)

    root.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))

    updateView(data, userCanvas, compCanvas)

    root.mainloop()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":

    ## Finally, run the simulation to test it manually ##
    runSimulation(500, 500) #
    #test.testDrawShip()