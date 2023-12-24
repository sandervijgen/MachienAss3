import tkinter as tk
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

WIDTH = 20 		#Breedte vd kamer 
HEIGHT = 20 		#Hoogte vd kamer
CELL_SIZE = 20 		#Pixelgrootte 10x10
ROBOT_LOC = []		#The location of the robot
BIN_LIST = []		#Here we will store the bin locations later on
G = nx.Graph()		#Create empty graph
MAP = [["." for _ in range(WIDTH)] for _ in range(HEIGHT)] #Vul kamer met 0=niks

def draw_map(canvas):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if MAP[y][x] == "O": # ROBOT
                color = "yellow"
            elif MAP[y][x] == "X": # BIN
                color = "red"
            elif MAP[y][x] == "#": # WALL
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
        MAP[row][col] = "#"

def makeWallY(col, start_row, end_row):
    global MAP
    start_row = max(0, start_row)
    end_row = min(len(MAP) - 1, end_row)
    for row in range(start_row, end_row + 1):
        MAP[row][col] = "#"

def placeBin(x,y,unWantedness): #quantification of how inapproprate it is for the robot to disturb at this location
	MAP[y][x] = "X"
	BIN_LIST.append((x,y,unWantedness))
	

def setRobotLocation(x, y):
    global ROBOT_LOC
    MAP[y][x] = "O" 
    ROBOT_LOC = [x, y]
    G.add_node("Robot")

def print_map():
    for row in MAP:
        print(' '.join(map(str, row)))

def find_shortest_path(start, end, grid): #BFS algorithm
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  #movement directions: right, left, down, up

    queue = deque([(start, 0)])  # Initialize queue with the starting position and distance
    visited = set()  # Keep track of visited cells

    while queue:
        current, distance = queue.popleft()  # Dequeue the current position and its distance

        if current == end:  # If we've reached the destination, return the distance
            return distance
        
        for dx, dy in directions:  # Check adjacent cells
            new_x, new_y = current[0] + dx, current[1] + dy
            
            if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid) and grid[new_y][new_x] != "#":
                new_pos = (new_x, new_y)
                if new_pos not in visited:
                    queue.append((new_pos, distance + 1))  # Enqueue new position with increased distance
                    visited.add(new_pos)  # Mark the new position as visited
                    
    return -1  # If no path is found

# Create your custom map here
# 1 represents the ROBOT and will be shown in YELLOW
# 2 represents a BIN and will be shown in RED
# 3 represents a WALL and will be shown in WHITE 
setRobotLocation(1,1)  # Robot 
placeBin(7,8,0)
placeBin(17,3,0)
placeBin(17,8,0)
placeBin(7,12,0)
placeBin(13,12,0)
placeBin(17,12,0)

makeWallX(10,2,15)
makeWallY(2,2,18)
makeWallY(9,2,18)
makeWallY(16,2,18)



# Create main window
root = tk.Tk()
root.title("2D Array Map")

# Create canvas
canvas = tk.Canvas(root, width=WIDTH * CELL_SIZE, height=HEIGHT * CELL_SIZE)
canvas.pack()

# Draw initial map
draw_map(canvas)

print("The user defined map looks as following:")
print_map()
print("The location of our robot is at: ",ROBOT_LOC)
print("The locations of the bins, with their level of unwantedness are: ",BIN_LIST)
'''
def find_shortest_paths_from_bins(robot_loc, bin_list, map):
    for bin_loc in bin_list:
        # Extract the first two elements from each tuple in bin_list
        bin_x, bin_y, unWantedness = bin_loc  # Extracting elements from the tuple
        shortest_path_length = find_shortest_path(robot_loc, (bin_x, bin_y), map)
        print(f"The shortest path length to bin {bin_loc[:2]} is: {shortest_path_length}")
'''
def find_shortest_paths_from_bins(robot_loc, bin_list, map):
    for index, bin_loc in enumerate(bin_list, start=1):
        # Extract the first two elements from each tuple in bin_list
        bin_x, bin_y, unWantedness = bin_loc  # Extracting elements from the tuple

        # Creating a new node for each bin
        node_name = f'Bin_{index}'  # Creating node names like 'Bin_1', 'Bin_2', etc.
        G.add_node(node_name, pos=(bin_x, bin_y))

        # Calculating the shortest path length
        shortest_path_length = find_shortest_path(robot_loc, (bin_x, bin_y), map)

        # Adding a weighted edge between the Robot node and the new bin node
        G.add_edge('Robot', node_name, weight=shortest_path_length)

        print(f"The shortest path length to bin {node_name} is: {shortest_path_length}")

find_shortest_paths_from_bins(ROBOT_LOC, BIN_LIST, MAP)

# Draw the graph
pos = nx.spring_layout(G)  # Position nodes using a spring layout
nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_weight='bold')

# Add edge labels
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Show the graph
plt.title('Weighted Graph Example')


#shortest_path_length = find_shortest_path(ROBOT_LOC, (7,12), MAP)
#print(f"The shortest path length is: {shortest_path_length}")

# Start GUI
root.mainloop()

plt.show()
