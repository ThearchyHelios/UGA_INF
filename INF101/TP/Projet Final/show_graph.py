'''
Author: JIANG Yilun
Date: 2021-11-27 14:37:13
LastEditTime: 2021-12-09 18:27:11
LastEditors: JIANG Yilun
Description: 
FilePath: /UGA_INF/INF101/TP/Projet Final/show_graph.py
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
    """ Cette méthode est utilisée pour lire la histoire locale

    Args:
        path (str): Le chemin correspondant au fichier

    Returns:
        dict: Retourner la histoire convertie
    """
    history = {}
    count = 0
    for line in open(path, "r"):
        line = line[:-1]  # delete \n
        # list_chaque_personne = f.split("\n")
        history[count] = {}
        item_list = line.split(",")
        history[count]["round"] = int(item_list[0])
        history[count]["difficulty"] = int(item_list[1])
        history[count]["croupier_premier_round"] = int(item_list[2])
        history[count]["croupier_value_final"] = int(item_list[3])
        history[count]["score"] = {}
        for score in item_list[4:-4]:
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
    global win_rate_global
    win_rate_global.clear()
    history = read_history("history.txt")
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
    win_rate_global.addItem(bargraph)


def graph_difficulty():
    global win_rate_difficulty
    win_rate_global.clear()
    history = read_history("history.txt")

    list_success_rate_easy = difficulty_easy(history)
    list_success_rate_normal = difficulty_normal(history)
    list_success_rate_hard = difficulty_hard(history)
    x = np.arange(17)
    x += 4
    win_rate_difficulty.plot(x, list_success_rate_easy, pen='r', name='Easy')
    win_rate_difficulty.plot(x, list_success_rate_normal, pen='g', name='Normal')
    win_rate_difficulty.plot(x, list_success_rate_hard, pen='b', name='Hard')


def difficulty_easy(history: dict) -> list:
    success_rate_list_point = []
    for number in range(4, 21):
        success = 0
        defayant = 0
        for item in history:
            temp_list_1 = []
            if history[item]["difficulty"] == 1:
                for key, item_score in history[item]["score"].items():
                    temp_list_1.append(int(item_score))
                if number in temp_list_1:
                    if history[item]["success"]:
                        success += 1
                    else:
                        defayant += 1
        success_rate_list_point.append(success / (success + defayant + 1))
    return success_rate_list_point


def difficulty_normal(history: dict) -> list:
    success_rate_list_point = []
    for number in range(4, 21):
        success = 0
        defayant = 0
        for item in history:
            temp_list_1 = []
            if history[item]["difficulty"] == 2:
                for key, item_score in history[item]["score"].items():
                    temp_list_1.append(int(item_score))
                if number in temp_list_1:
                    if history[item]["success"]:
                        success += 1
                    else:
                        defayant += 1
        success_rate_list_point.append(success / (success + defayant + 1))
    return success_rate_list_point


def difficulty_hard(history: dict) -> list:
    success_rate_list_point = []
    for number in range(4, 21):
        success = 0
        defayant = 0
        for item in history:
            temp_list_1 = []
            if history[item]["difficulty"] == 3:
                for key, item_score in history[item]["score"].items():
                    temp_list_1.append(int(item_score))
                if number in temp_list_1:
                    if history[item]["success"]:
                        success += 1
                    else:
                        defayant += 1
        success_rate_list_point.append(success / (success + defayant + 1))
    return success_rate_list_point


if __name__ == "__main__":
    history = read_history("history.txt")
    win_rate_global = pg.plot()
    win_rate_global.setWindowTitle('Win Rate live')
    win_rate_difficulty = pg.plot()
    win_rate_difficulty.setWindowTitle('Win Rate of 3 difficulty')
    graph_difficulty()
    timer = pg.QtCore.QTimer()
    timer.timeout.connect(show_history)
    timer.start(1000)
    pg.exec()
