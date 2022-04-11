/*
 * @Author: JIANG Yilun
 * @Date: 2022-03-28 15:55:44
 * @LastEditTime: 2022-03-28 16:42:54
 * @LastEditors: JIANG Yilun
 * @Description: 
 * @FilePath: /UGA_INF/INF203/Language C/semaine 8/Exercice8.c
 */

#include <stdio.h>

int a_in_b (int a[], int b[], int nA, int nB){
    int i;
    int j;
    int count = 0;
    for (i=0; i<nA; i++){
        for (j=0; j<nB; j++){
            if (a[i] == b[j]){
                count += 1;
            }
        }
    }
    if (count == nA || count == nB){
        return 1;
    }
    else{
        return 0;
    }
}

int a_and_b (int a[], int b[], int nA, int nB){
    int size_list = nA + nB;
    int list[size_list];
    for (int i=0; i<nA; i++){
        for (int j=0; j<nB; j++){
            if (b[j] <= a[i]){
                list[i] = b[j];
            } else {
                list[i] = a[i];
            }
        }
    }
    return list;
}

int main(){
    int a[] = {1,2,3,8};
    int b[] = {1,2,3,4,5,6,7};

    if (a_in_b(a, b, 4, 7)){
        printf("a est dans b\n");
    } else {
        printf("a n'est pas dans b\n");
    }
    int return_list = a_and_b(a, b, 4, 7);
    for (int i=0; i<11; i++){
        printf(return_list[i]);
    }
    return 0;
}