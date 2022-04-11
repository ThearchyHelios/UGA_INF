/*
 * @Author: JIANG Yilun
 * @Date: 2022-04-04 15:43:38
 * @LastEditTime: 2022-04-04 16:36:54
 * @LastEditors: JIANG Yilun
 * @Description: Exercice1.c
 * @FilePath: /UGA_INF/INF203/Language C/semaine 9/Exercice1.c
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

int main()
{
    int score_list[2];
    int i, j;
    for (i = 0; i < 2; i++)
    {
        score_list[i] = 0;
    }
    for (;;)
    {
        srand((unsigned int)time(0));
        for (int i = 0; i < 600000; i++)
        {
            printf("This is the %dth round\n", i + 1);
            int zero_or_one = rand() % 2;
            printf("%d", zero_or_one);
            if (zero_or_one == 1)
            {
                score_list[0] += 1;
            }
            else
            {
                score_list[1] += 1;
            }
            
        }

        if (score_list[0] - score_list[1] > 2 || score_list[1] - score_list[0] > 2)
        {
            break;
        }
    }
    printf("Le score de a est de %d\n", score_list[0]);
    printf("Le score de b est de %d\n", score_list[1]);
}