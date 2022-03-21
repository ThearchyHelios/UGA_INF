/*
 * @Author: JIANG Yilun
 * @Date: 2022-03-21 15:19:40
 * @LastEditTime: 2022-03-21 19:40:52
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
    // if (argc = 1){
    //     printf("Il y a %d caracteres dans le fichier %s\n", nb_character(stdin));
    // }
    for (int i = 1; i < argc; i++)
    {
        FILE *f = fopen(argv[i], "r");
        if (f == NULL)
        {
            printf("Erreur dans l'ouverture du fichier %s\n", argv[i]);
            return 1;
        }
        else
        {
            printf("Il y a %d caracteres dans le fichier %s\n", nb_character(f), argv[i]);
            fclose(f);
        }

        return 0;
    }
}