'''
Author: JIANG Yilun
Date: 2021-11-27 14:37:13
LastEditTime: 2021-11-27 14:38:46
LastEditors: JIANG Yilun
Description: 
FilePath: /INF_101/INF101/TP/Projet Final/show_graph.py
'''

import distutils.core
from unittest import result
import matplotlib.pyplot as plt
import os.path
from pandas import period_range
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np


def read_history(path):
    history = {}
    count = 0
    for line in open(path, "r"):
        line = line[:-1]  # delete \n
        # list_chaque_personne = f.split("\n")
        history[count] = {}
        item_list = line.split(",")
        history[count]["round"] = int(item_list[0])
        history[count]["croupier_premier_round"] = int(item_list[1])
        history[count]["croupier_value_final"] = int(item_list[2])
        history[count]["score"] = {}
        for score in item_list[3:-4]:
            list_temp = score.split(":")
            history[count]["score"][list_temp[0]] = int(list_temp[1])
        history[count]["success"] = bool(
            distutils.util.strtobool(item_list[-4]))
        history[count]["out"] = bool(distutils.util.strtobool(item_list[-3]))
        history[count]["give_up"] = bool(
            distutils.util.strtobool(item_list[-2]))
        history[count]["draw"] = bool(distutils.util.strtobool(item_list[-1]))
        count += 1
    return history

def show_history():
    global win_rate
    win_rate.clear()
    history = read_history("INF101/TP/Projet Final/history.txt")
    x = np.arange(17)
    x += 4
    success_rate_list_point = []
    for number in range(4, 21):
        success = 0
        defayant = 0
        for item in history:
            temp_list_1 = []
            for key, item_score in history[item]["score"].items():
                temp_list_1.append(int(item_score))
            if number in temp_list_1:
                if history[item]["success"]:
                    success += 1
                else:
                    defayant += 1
        success_rate_list_point.append(success / (success + defayant + 1))
    bargraph = pg.BarGraphItem(x=x,
                               height=success_rate_list_point,
                               width=1,
                               brush='b')
    win_rate.addItem(bargraph)




if __name__ == "__main__":
    history = read_history("INF101/TP/Projet Final/history.txt")
    win_rate = pg.plot()
    win_rate.setWindowTitle('Win Rate Bar Graph')
    timer = pg.QtCore.QTimer()
    timer.timeout.connect(show_history)
    timer.start(1000)
    pg.exec()