/*
 * @Author: JIANG Yilun
 * @Date: 2022-03-17 15:35:58
 * @LastEditTime: 2022-03-17 16:02:03
 * @LastEditors: JIANG Yilun
 * @Description:
 * @FilePath: /UGA_INF/INF203/Language C/test.c
 */

#include <stdio.h>
void echange(int Tab[], int i, int j)
{
    int tmp;
    tmp = Tab[i];
    Tab[i] = Tab[j];
    Tab[j] = tmp;
}
int main()
{
    // Initialisation de taille et valeurs
    int Tab[] = {42, 203};
    echange(Tab, 0, 1);
    printf("En %d on parle de %d\n", Tab[0], Tab[1]);
    return 0;
}