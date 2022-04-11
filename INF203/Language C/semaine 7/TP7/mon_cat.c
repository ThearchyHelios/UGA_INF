/*
 * @Author: JIANG Yilun
 * @Date: 2022-03-24 15:32:52
 * @LastEditTime: 2022-03-28 15:29:32
 * @LastEditors: JIANG Yilun
 * @Description:
 * @FilePath: /UGA_INF/INF203/Language C/semaine 7/TP7/mon_cat.c
 */
#include <stdio.h>

int main(int argc, char *argv[])
{
	FILE *f;
	char c;

	f = fopen(argv[1], "r");
	if (f == NULL)
	{
		printf("%s n'a pas pu être ouvert en lecture\n", argv[1]);
		return 1;
	}
	fscanf(f, "%c", &c);
	while (!feof(f))
	{
		printf("%c", c);
		fscanf(f, "%c", &c);
	}

	fclose(f);
	return 0;
}
