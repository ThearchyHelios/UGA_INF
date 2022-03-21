/*
 * @Author: JIANG Yilun
 * @Date: 2022-03-21 15:31:12
 * @LastEditTime: 2022-03-21 15:45:35
 * @LastEditors: JIANG Yilun
 * @Description:
 * @FilePath: /UGA_INF/INF203/Language C/semaine 7/Exercice1.c
 */

#include <stdio.h>

// int main(int argc, char *argv[])
// {
//     printf("argc vaut %d\n", argc);
//     for (int i = 1; i <= argc; i++)
//     {
//         int valeur;
//         printf("L'argument %d vaut %s", i, argv[i]);
//         if (sscanf(argv[i], "d", &valeur) == 1)
//             printf(" qui vaut %d\n", valeur);
//         else
//             printf(" qui n'est pas un entier\n");
//     }
//     return 0;
// }

int main(int argc, char *argv[])
{
    int somme = 0;
    for (int i = 1; i < argc; i++)
    {
        int entier;
        if (sscanf(argv[i], "%d", &entier) == 1)
        {
            somme += entier;
        }
    }
    printf("%d\n", somme);

    return 0;
}