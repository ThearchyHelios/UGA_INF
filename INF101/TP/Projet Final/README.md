<!--
 * @Author: JIANG Yilun
 * @Date: 2021-12-06 09:15:35
 * @LastEditTime: 2021-12-15 09:03:28
 * @LastEditors: JIANG Yilun
 * @Description: 
 * @FilePath: /UGA_INF/INF101/TP/Projet Final/README.md
-->
# RAPPORT
```python
def tourJoueur(liste_pioche, j, scores, score_croupier_premier_round):
    """ Cette fonction lance un nouveau tour de jeu et peut afficher le nombre de tours passés, le scores de tous les joueurs, et celui de ceux encore en jeu.
    Args:
        j (str): Nom du joueur
        scores (dict): Scores des joueurs
        score_croupier_premier_round (int): Score du croupier au premier tour
    """

    score = 0
    round = 0
    liste_score = []

    score = scores[j]["score"]
    round = scores[j]["round"]
    for nom in scores:
        for nom_item, item in scores[nom].items():
            if nom_item == "score":
                liste_score.append(item)

    round += 1
    scores[j]["round"] = round
    print("--------------------")
    print("Tour %s" % round)
    print("%s, a vous de jouer." % j)
    for i in range(len(liste_score)):
        if i == 0:
            print("Il y a %s joueurs qui on respectivement %s " %
                  (len(liste_score), liste_score[i]),
                  end="")
        elif i == len(liste_score) - 1:
            print("%s points." % liste_score[i])
        else:
            print("%s " % liste_score[i], end="")
    print("Le croupier a %s points." % score_croupier_premier_round)

    scores[j]["history"]["round %s" % round] = score
    print("Votres score est de %s points." % score)

    if not scores[j]["ordi"]:
        if joueur_continuer():
            if liste_pioche == []:
                liste_pioche = initPioche(len(scores))
            liste_carte = piocheCarte(liste_pioche, 1)
            for carte in liste_carte:
                print("Voici la carte que vous avez pioché : %s" % carte)
                temp = int(valeurCarte(carte))
                if temp == 0:
                    if scores[j]["score"] < 12:
                        temp = 11
                    else:
                        temp = 1
                score += temp
            print("Votre score est de %s points." % score)
            scores[j]["score"] = score
            if score > 21:
                print("Vous avez perdu!")
                scores[j]["out"] = True
                scores[j]["history"]["round %s" % (round + 1)] = score
            if score == 21:
                scores[j]["give_up"] = True
                scores[j]["history"]["round %s" % (round + 1)] = score

        else:
            scores[j]["give_up"] = True
            print("Votre tour est términé.")
        time.sleep(2)

    elif scores[j]["ordi"]:
        if bot_decision(liste_pioche, scores, j):
            if liste_pioche == []:
                liste_pioche = initPioche(len(scores))
            liste_carte = piocheCarte(liste_pioche, 1)
            for carte in liste_carte:
                print("Voici la carte que vous avez pioché : %s" % carte)
                temp = int(valeurCarte(carte))
                if temp == 0:
                    if scores[j]["score"] < 12:
                        temp = 11
                    else:
                        temp = 1
                score += temp
            print("Votre score est de %s points." % score)
            scores[j]["score"] = score
            if score > 21:
                print("Vous avez perdu!")
                scores[j]["out"] = True
                scores[j]["history"]["round %s" % (round + 1)] = score
            if score == 21:
                scores[j]["give_up"] = True
                scores[j]["history"]["round %s" % (round + 1)] = score

            time.sleep(2)

        else:
            scores[j]["give_up"] = True
            print("Votre tour est términé.")

        time.sleep(2)

```