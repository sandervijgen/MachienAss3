from collections import deque

def find_shortest_path(start, end, grid):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Define possible movement directions: right, left, down, up
    
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
                    queue.append((new_pos, distance + 1))  # Enqueue the new position with increased distance
                    visited.add(new_pos)  # Mark the new position as visited
                    
    return -1  # If no path is found

# Example grid (MAP)
MAP = [
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "O", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", "#", ".", ".", ".", ".", ".", ".", "#", ".", ".", ".", ".", ".", ".", ".", ".", "#", "."],
    [".", ".", "#", ".", ".", ".", ".", ".", ".", "#", ".", ".", ".", ".", ".", ".", "X", ".", "#", "."],
    # ... (other rows of the map)
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
]

# Start and end positions
start_position = (1, 1)  # The "O" is at array cell [1, 1]
end_position = (17, 3)  # For example, one of the "X" positions

# Find the shortest path
shortest_path_length = find_shortest_path(start_position, end_position, MAP)
print(f"The shortest path length is: {shortest_path_length}")

