/*
 * @Author: JIANG Yilun
 * @Date: 2022-03-21 15:19:40
 * @LastEditTime: 2022-03-21 16:39:43
 * @LastEditors: JIANG Yilun
 * @Description:
 * @FilePath: /UGA_INF/INF203/Language C/semaine 7/Exercice2.c
 */

#include <stdio.h>
// int wc(char *s)
// {
//     int i = 0;
//     int count = 0;
//     while (s[i] != '\0')
//     {
//         if (s[i] != ' ' || s[i] != '\n')
//         {
//             count++;
//         }
//         i++;
//     }
//     return count;
// }

// int main()
// {
//     char s[100];
//     printf("Entrez une chaine de caractere: ");
//     scanf("%s", s);
//     // scanf 只能读取一个字符串
//     printf("Il y a %d mots dans la chaine\n", wc(s));
//     return 0;
// }

int nb_character(FILE *f)
{
    int compteur = 0;
    char c;

    fscanf(f, "%c", &c);
    while (!feof(f))
    {
        compteur++;
        fscanf(f, "%c", &c);
    }
    return compteur;
}

int main(int argc, char *argv[])
{
    FILE *f = fopen(argv[1], "r");
    if (f == NULL)
    {
        printf("Erreur d'ouverture du fichier\n");
        return 1;
    }
    else
    {
        printf("Il y a %d caracteres dans le fichier\n", nb_character(f));
        fclose(f);
        return 0;
    }
}