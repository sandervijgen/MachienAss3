import tkinter as tk

WIDTH = 50 		#Breedte vd kamer 
HEIGHT = 25 		#Hoogte vd kamer
CELL_SIZE = 20 		#Pixelgrootte 10x10
MAP = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)] #Vul kamer met 0=niks

def draw_map(canvas):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if MAP[y][x] == 1: # ROBOT
                color = "yellow"
            elif MAP[y][x] == 2: # BIN
                color = "red"
            elif MAP[y][x] == 3: # WALL
                color = "white"
            else:
                color = "black"
                
            canvas.create_rectangle(
                x * CELL_SIZE,
                y * CELL_SIZE,
                (x + 1) * CELL_SIZE,
                (y + 1) * CELL_SIZE,
                fill=color,
                outline=""
            )

def makeWallX(row, start_col, end_col):
    global MAP 
    start_col = max(0, start_col)
    end_col = min(len(MAP[0]) - 1, end_col)
    for col in range(start_col, end_col + 1):
        MAP[row][col] = 3

def makeWallY(col, start_row, end_row):
    global MAP
    start_row = max(0, start_row)
    end_row = min(len(MAP) - 1, end_row)
    for row in range(start_row, end_row + 1):
        MAP[row][col] = 3

def placeBin(x,y):
	MAP[y][x] = 2

# Create your custom map here
# 1 represents the ROBOT and will be shown in YELLOW
# 2 represents a BIN and will be shown in RED
# 3 represents a WALL and will be shown in WHITE 
MAP[1][1] = 1  # Robot 
placeBin(7,8)
placeBin(17,8)
placeBin(27,8)
placeBin(7,12)
placeBin(13,12)
placeBin(17,12)

makeWallX(10,5,25)
makeWallY(5,5,15)
makeWallY(15,5,20)
makeWallY(25,5,15)


# Create main window
root = tk.Tk()
root.title("2D Array Map")

# Create canvas
canvas = tk.Canvas(root, width=WIDTH * CELL_SIZE, height=HEIGHT * CELL_SIZE)
canvas.pack()

# Draw initial map
draw_map(canvas)

# Start GUI
root.mainloop()

