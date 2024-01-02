import numpy as np

# Define the graph with nodes and edge weights
nodes = ['Robot', 'Bin_1', 'Bin_2', 'Bin_3', 'Bin_4', 'Bin_5', 'Bin_6']
amount_of_nodes = len(nodes)

# Define the graph's edge weights
edges = {
    ('Robot', 'Bin_1'): 13, ('Robot', 'Bin_2'): 18, ('Robot', 'Bin_3'): 23, ('Robot', 'Bin_4'): 31,
    ('Robot', 'Bin_5'): 37, ('Robot', 'Bin_6'): 27, ('Bin_1', 'Bin_2'): 19, ('Bin_1', 'Bin_3'): 24,
    ('Bin_1', 'Bin_4'): 44, ('Bin_1', 'Bin_5'): 46, ('Bin_1', 'Bin_6'): 28, ('Bin_2', 'Bin_3'): 5,
    ('Bin_2', 'Bin_4'): 33, ('Bin_2', 'Bin_5'): 27, ('Bin_2', 'Bin_6'): 9, ('Bin_3', 'Bin_4'): 28,
    ('Bin_3', 'Bin_5'): 22, ('Bin_3', 'Bin_6'): 4, ('Bin_4', 'Bin_5'): 20, ('Bin_4', 'Bin_6'): 24,
    ('Bin_5', 'Bin_6'): 18, ('Robot', 'Robot'): 0, ('Bin_1', 'Bin_1'): 0, ('Bin_2', 'Bin_2'): 0,
    ('Bin_3', 'Bin_3'): 0, ('Bin_4', 'Bin_4'): 0, ('Bin_5', 'Bin_5'): 0, ('Bin_6', 'Bin_6'): 0,
    ('Bin_1', 'Robot'): 13, ('Bin_2', 'Robot'): 18, ('Bin_3', 'Robot'): 23, ('Bin_4', 'Robot'): 31,
    ('Bin_5', 'Robot'): 37, ('Bin_6', 'Robot'): 27, ('Bin_2', 'Bin_1'): 19, ('Bin_3', 'Bin_1'): 24,
    ('Bin_4', 'Bin_1'): 44, ('Bin_5', 'Bin_1'): 46, ('Bin_6', 'Bin_1'): 28, ('Bin_3', 'Bin_2'): 5,
    ('Bin_4', 'Bin_2'): 33, ('Bin_5', 'Bin_2'): 27, ('Bin_6', 'Bin_2'): 9, ('Bin_4', 'Bin_3'): 28,
    ('Bin_5', 'Bin_3'): 22, ('Bin_6', 'Bin_3'): 4, ('Bin_5', 'Bin_4'): 20, ('Bin_6', 'Bin_4'): 24,
    ('Bin_6', 'Bin_5'): 18
}

# Create a matrix to represent the Q-values initialized with zeros
Q = np.zeros((amount_of_nodes, amount_of_nodes))

# Set gamma (discount factor) and learning rate
gamma = 0.55
learning_rate = 0.55

# Define the number of episodes for training
amount_of_episodes = 500

# Q-learning algorithm
for _ in range(amount_of_episodes):
    # Start from a random node (Robot)
    current_state = np.random.randint(0, amount_of_nodes)
    while current_state != nodes.index('Bin_6'):  # Loop until the final state (last bin) is reached
        # Select a random next state with non-zero Q-value
        possible_actions = []
        for i, q_value in enumerate(Q[current_state]):
            if q_value >= 0:
                possible_actions.append(i)
        next_state = np.random.choice(possible_actions)

        # Calculate the maximum Q-value for the next state
        max_next_q = np.max(Q[next_state])

        # Update Q-value using Q-learning formula
        Q[current_state, next_state] = (1 - learning_rate) * Q[current_state, next_state] + learning_rate * (edges[(nodes[current_state], nodes[next_state])] + gamma * max_next_q)

        # Move to the next state
        current_state = next_state

# Find the optimal path
current_state = 0  # Start from Robot node
optimal_path = [nodes[current_state]]  # Store the optimal path

def set_column_to_zero(arr, column_index):
    for row in arr:
        row[column_index] = 0

while current_state != nodes.index('Bin_6'):
    set_column_to_zero(Q, current_state)
    next_state = np.argmax(Q[current_state])  # Select the next state with the highest Q-value
    optimal_path.append(nodes[next_state])  # Add the next node to the optimal path
    current_state = next_state

print("Optimal Path:", optimal_path)
