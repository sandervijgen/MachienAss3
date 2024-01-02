import gym
import numpy as np

env = gym.make('MountainCar-v0', render_mode="human")

LEARNING_RATE = 0.1 # Hoeveel we leren per actie
DISCOUNT = 0.95 # Hoeveel waarde hechten we aan toekomstige acties vs huidige acties
EPISODES = 25000 # Hoeveel keer gaan we het spel spelen

SHOW_EVERY = 200 # Hoe vaak laten we het spel zien

print(env.observation_space.high)
print(env.observation_space.low)
print(env.action_space.n)

DISCRETE_OS_SIZE = [20] * len(env.observation_space.high) # Maak de observatie ruimte discreet
discrete_os_win_size = (env.observation_space.high - env.observation_space.low) / DISCRETE_OS_SIZE # Bepaal de grootte van de discrete observatie ruimte

q_table = np.random.uniform(low=-2, high=0, size=(DISCRETE_OS_SIZE + [env.action_space.n])) # Maak een q-table aan met de grootte van de discrete observatie ruimte en het aantal acties

def get_discrete_state(state):
    discrete_state = (state - env.observation_space.low) / discrete_os_win_size # Bepaal de discrete state
    return tuple(discrete_state.astype(np.int)) # Return de discrete state

for episode in range(EPISODES):
    if episode % SHOW_EVERY == 0:
        print(episode)
        render = True
    else:
        render = False

    discrete_state = get_discrete_state(env.reset()) # Bepaal de discrete state van de initiële state
    done = False
    while not done:
        action = np.argmax(q_table[discrete_state]) # Bepaal de actie die de grootste reward heeft
        new_state, reward, done, truncation, _ = env.step(action) # Voer de actie uit
        done = truncation
        new_discrete_state = get_discrete_state(new_state) # Bepaal de nieuwe discrete state
        if render:
            env.render() # Render de omgeving
        if not done:
            max_future_q = np.max(q_table[new_discrete_state]) # Bepaal de grootste reward van de nieuwe discrete state
            current_q = q_table[discrete_state + (action,)] # Bepaal de reward van de huidige discrete state
            new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q) # Bepaal de nieuwe reward (formule)
            q_table[discrete_state + (action,)] = new_q
        elif new_state[0] >= env.goal_position:
            print(f"We made it on episode {episode}")
            q_table[discrete_state + (action,)] = 0

        discrete_state = new_discrete_state # Update de discrete state

env.close()