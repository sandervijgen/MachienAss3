import os
import time
import gym
from pygame.time import delay
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy

environment_name = 'CartPole-v0'
env = gym.make(environment_name, render_mode="human")

episodes = 10  # aantal keer spelen van het spel (hoe meer hoe beter)
for episodes in range(1, episodes + 1):
    state = env.reset()
    done = False
    score = 0

    while not done:
        env.render()  # laat de omgeving zien via gui (kan ook zonder)
        action = env.action_space.sample()  # kies een random actie uit de actie ruimte (0 of 1)
        n_state, reward, done, info, _ = env.step(action)
        score += reward
    print('Episode:{} Score:{}'.format(episodes, score))
env.close()

log_path = os.path.join('Training', 'Logs')
log_path
env = gym.make(environment_name) # maak de omgeving aan (CartPole-v0)
env = DummyVecEnv([lambda: env]) # maak een omgeving aan met een vector van 1 omgeving (deze is nodig voor stable baselines)
model = PPO('MlpPolicy', env, verbose=1, tensorboard_log=log_path) # maak een model aan met de PPO algoritme, de MlpPolicy, de omgeving en de log path

model.learn(total_timesteps=1000) # train het model met 20000 timesteps (hoe meer hoe beter)





PPO_Path = os.path.join('Training', 'Saved Models', 'PPO_Model_CartPole') # maak een path aan voor het opslaan van het model
model.save(PPO_Path) # sla het model op
#del model # verwijder het model om te laten zien dat het model opnieuw geladen kan worden zonder te trainen
PPO_Path
model.learn(total_timesteps=1000) # train het model met 20000 timesteps (hoe meer hoe beter)
model = PPO.load(PPO_Path, env=env) # laad het model

evaluate_policy(model, env, n_eval_episodes=10, render=True) # evalueer het model

env.close() # sluit de omgeving

### TEST

episodes = 5  # aantal keer spelen van het spel (hoe meer hoe beter)
for episodes in range(1, episodes + 1):
    obs = env.reset()
    done = False
    score = 0

    while not done:
        env.render()  # laat de omgeving zien via gui (kan ook zonder)
        action = model.predict(obs)
        obs, reward, done, info, _ = env.step(action)
        score += reward
    print('Episode:{} Score:{}'.format(episodes, score))
#env.close()

obs= env.reset()
model.predict(obs)