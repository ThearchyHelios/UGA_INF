'''
Author: JIANG Yilun
Date: 2021-11-18 23:10:12
LastEditTime: 2021-11-20 19:56:48
LastEditors: JIANG Yilun
Description: 
FilePath: /INF_101/INF101/TP/Projet Final/method_test.py
'''
# import random
# total = [10, 100, 1000, 10000, 100000, 1000000, 5000000, 10000000, 100000000]  #随机点数
# for t in total:
#     in_count = 0
#     for i in range(t):
#         x = random.random()
#         y = random.random()
#         dis = (x**2 + y**2)**0.5
#         if dis<=1:
#             in_count += 1
#     print(t,'个随机点时，π是：', 4*in_count/t)'

import sys
import gym
import numpy as np
from collections import defaultdict

from plot_utils import plot_blackjack_values, plot_policy


env = gym.make('Blackjack-v0')

print(env.observation_space)
print(env.action_space)

for i_episode in range(3):
    state = env.reset()
    while True:
        print(state)
        action = env.action_space.sample()
        state, reward, done, info = env.step(action)
        if done:
            print('End game! Reward: ', reward)
            print('You won :)\n') if reward > 0 else print('You lost :(\n')
            break
