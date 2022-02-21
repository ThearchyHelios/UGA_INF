'''
Author: JIANG Yilun
Date: 2022-02-21 15:13:14
LastEditTime: 2022-02-21 15:16:30
LastEditors: JIANG Yilun
Description: 
FilePath: /UGA_INF/INF101/TP/TP6/2.6.1.4_mirror.py
'''
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
temp = []
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    temp.append(t)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

def proche_zero(list):
    try:
        temp_temperature = list[0]
        for i in range(len(list)):
            if abs(list[i]) < abs(temp_temperature):
                temp_temperature = list[i]
            if abs(list[i]) == abs(temp_temperature):
                if list[i] > temp_temperature:
                    temp_temperature = list[i]
    except:
        print("0")
    return temp_temperature


print(proche_zero(temp))