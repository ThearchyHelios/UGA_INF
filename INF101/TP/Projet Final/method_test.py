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

import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from