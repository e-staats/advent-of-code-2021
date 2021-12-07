#include <stdio.h>
#include <stdlib.h>

int main(void)
{

    char s[1024];
    FILE *fp;
    fp = fopen("../inputs/day1.txt", "r");
    int count = 0;
    int linecount = 0;
    long window1 = 0;
    long window2 = 0;
    long d1 = 0;
    long d2 = 0;
    long d3 = 0;
    long d4 = 0;

    d1 = strtol(fgets(s, sizeof s, fp), NULL, 10);
    d2 = strtol(fgets(s, sizeof s, fp), NULL, 10);
    d3 = strtol(fgets(s, sizeof s, fp), NULL, 10);
    while (fgets(s, sizeof s, fp) != NULL)
    {
        d4 = strtol(s, NULL, 10);
        window1 = d1 + d2 + d3;
        window2 = d2 + d3 + d4;
        if (window2 > window1) { count++; }
        d1 = d2;
        d2 = d3;
        d3 = d4;
    }

    fclose(fp);
    printf("count: %d\n", count);
}
