import gymnasium as gym
import gym_mtsim
from stable_baselines3 import SAC


if __name__ == '__main__':
    env = gym.make('forex-unhedge-v0')
    model = SAC(env=env, policy='MultiInputPolicy', verbose=1)
    model.learn(1000_000)

