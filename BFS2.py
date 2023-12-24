from collections import deque

def find_shortest_path(start, end, grid):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Define possible movement directions: right, left, down, up
    
    queue = deque([(start, [])])  # Initialize queue with the starting position and an empty path
    visited = set()  # Keep track of visited cells
    
    while queue:
        current, path = queue.popleft()  # Dequeue the current position and its path
        
        if current == end:  # If we've reached the destination, return the path
            return path
        
        for dx, dy in directions:  # Check adjacent cells
            new_x, new_y = current[0] + dx, current[1] + dy
            
            if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid) and grid[new_y][new_x] != "#":
                new_pos = (new_x, new_y)
                if new_pos not in visited:
                    queue.append((new_pos, path + [new_pos]))  # Enqueue the new position with updated path
                    visited.add(new_pos)  # Mark the new position as visited
                    
    return []  # If no path is found, return an empty list

# Example grid (MAP)
# (Your MAP grid)
MAP = [
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "O", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", "#", ".", ".", ".", ".", ".", ".", "#", ".", ".", ".", ".", ".", ".", ".", ".", "#", "."],
    [".", ".", "#", ".", ".", ".", ".", ".", ".", "#", ".", ".", ".", ".", ".", ".", "X", ".", "#", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
]
# Start and end positions
start_position = (1, 1)  # The "O" is at array cell [1, 1]
end_position = (17, 3)  # For example, one of the "X" positions

# Find the shortest path
shortest_path = find_shortest_path(start_position, end_position, MAP)
if shortest_path:
    print(f"The shortest path is: {shortest_path}")
    for cell in shortest_path:
        x, y = cell
        print(f"Cell ({x}, {y})")
else:
    print("No path found.")

