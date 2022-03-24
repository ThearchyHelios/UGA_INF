/*
 * @Author: JIANG Yilun
 * @Date: 2022-03-24 15:32:52
 * @LastEditTime: 2022-03-24 16:01:40
 * @LastEditors: JIANG Yilun
 * @Description: 
 * @FilePath: /UGA_INF/INF203/Language C/semaine 7/TP7/somme.c
 */
#include<stdio.h>

int main (int argc, char *argv[]) {

  printf("%s", argv[1]);
  for (int i=2 ; i<argc; i++){
    printf(" + %s",argv[i]);
  }

  printf(" = ");
  int count = 0;
  for (int i=1; i<argc; i++){
    // count = (int)argv[i] + count;
    int temp;
    sscanf(argv[i], "%d", &temp);
    count += temp;
  }
  printf("%d\n", count);
  return 0;
}
