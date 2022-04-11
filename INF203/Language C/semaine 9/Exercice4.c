/*
 * @Author: JIANG Yilun
 * @Date: 2022-04-04 16:43:30
 * @LastEditTime: 2022-04-04 16:45:15
 * @LastEditors: JIANG Yilun
 * @Description:
 * @FilePath: /UGA_INF/INF203/Language C/semaine 9/Exercice4.c
 */

#include <stdio.h>
#include <ctype.h>
#define LETTRE 0
#define PONCTUATION 1
#define ESPACE 2
#define FIN_FICHIER 3

int transition[4][4] = {{1, 2, 2, 3},
                        {1, 2, 2, 3},
                        {1, 2, 2, 3},
                        {3, 3, 3, 3}};
int lire_nature_entree(FILE *f)
{
    char c;
    int nature;
    fscanf(f, "%c", &c);
    if (feof(f))
        nature = FIN_FICHIER;
    else if (isalpha(c))
        nature = LETTRE;
    else if (isspace(c))
        nature = ESPACE;
    else
        nature = PONCTUATION;
    return nature;
}
int sortie(int etat, int nature_entree)
{
    int bip = 0;
    if ((etat == 1) && (nature_entree != LETTRE))
        bip = 1;
    return bip;
}
int main(int argc, char *argv[])
{
    FILE *f;
    int x;
    int etat_courant, etat_suivant;
    int nature_entree;
    /* Verification du nombre d’arguments, ouverture du fichier avec verification */ 
    /* -> A COMPLETER */
    
    /* Simulation */
    /* -> A COMPLETER */
    printf("x = %d\n", x);
    return 0;
}