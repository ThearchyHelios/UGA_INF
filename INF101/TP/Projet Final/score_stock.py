'''
Author: JIANG Yilun
Date: 2021-11-17 21:06:25
LastEditTime: 2021-11-20 20:12:33
LastEditors: JIANG Yilun
Description: 
FilePath: /INF_101/users/yilunjiang/github/inf_101/inf101/tp/projet final/score_stock.py
'''
# TODO: 修改score列表，使得可以获取历史数据
# TODO：将历史数据写入表格中


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
        if count_round == 1:
            continue
        for items in scores[nom]:
            if scores[nom]["success"]:
                success = True
            if scores[nom]["out"]:
                out = True
            if scores[nom]["give_up"]:
                give_up = True
        for key, items in scores[nom]["history"].items():
            history = history + str(key) + ":" + str(items) + ","

        string = str(count_round) + "," + history + str(success) + "," + str(
            out) + "," + str(give_up) + "\n"
        with open(path, 'a+') as f:
            f.write(string)
            f.close()
