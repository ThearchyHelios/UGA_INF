/*
 * @Author: JIANG Yilun
 * @Date: 2022-03-24 15:32:52
 * @LastEditTime: 2022-03-24 15:33:25
 * @LastEditors: JIANG Yilun
 * @Description: 
 * @FilePath: /UGA_INF/INF203/Language C/semaine 7/TP7/aff_arg.c
 */
#include<stdio.h>

int main (int argc, char *argv[]) {
  int i ;

  printf("\nargc : %d\n\n",argc);

  for (i=0 ; i<argc ; i++)
    printf("l'argument numero %d est %s\n",i, argv[i]) ;

  printf("\n");
  return 0;
}
