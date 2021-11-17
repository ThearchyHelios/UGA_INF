# TODO: 修改score列表，使得可以获取历史数据
# TODO：将历史数据写入表格中
import numpy as np


def history_save_to_txt(path, scores):
    # liste_histoire = {}
    # for nom in scores:
    #     for key, items in scores[nom]["history"].items():
    #         liste_histoire[nom][key] = items
    for nom in scores:
        count_round = len(scores[nom]["history"])
        success = False
        out = False
        give_up = False
        history = ""
        for items in scores[nom]:
            if scores[nom]["success"]:
                success = True
            if scores[nom]["out"]:
                out = True
            if scores[nom]["give_up"]:
                give_up = True
        for key, items in scores[nom]["history"].items():
            history = history + str(key) + ":" + str(items) + ","

        string = str(count_round) + "," + history + str(success) + "," + str(out) + str(give_up) + "\n"
        with open(path, 'a+') as f:
            f.write(string)
            f.close()
