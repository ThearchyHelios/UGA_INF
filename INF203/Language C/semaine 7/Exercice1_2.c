/*
 * @Author: JIANG Yilun
 * @Date: 2022-03-21 15:55:19
 * @LastEditTime: 2022-03-21 16:04:00
 * @LastEditors: JIANG Yilun
 * @Description:
 * @FilePath: /UGA_INF/INF203/Language C/semaine 7/Exercice1_2.c
 */

#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    int entier1, entier2, resultat;
    sscanf(argv[1], "%d", &entier1);
    sscanf(argv[3], "%d", &entier2);

    if (argc != 4)
    {
        printf("Erreur dans le nombre d'arguments\nIl faut 3 arguments");
        return 1;
    }

    if (strcmp(argv[2], "+"))
    {
        resultat = entier1 + entier2;
    }
    else if (strcmp(argv[2], "-"))
    {
        resultat = entier1 - entier2;
    }
    else if (strcmp(argv[2], "*"))
    {
        resultat = entier1 * entier2;
    }
    else if (strcmp(argv[2], "/"))
    {
        resultat = entier1 / entier2;
    }
    else
    {
        resultat = 0;
    }
    printf("%d\n", resultat);
}