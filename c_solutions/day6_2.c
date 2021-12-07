#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h> // for time()

int main(void)
{

    double time_spent = 0.0;
    clock_t begin = clock();

    FILE *fp;
    char s[1024];
    char delim[] = ",";
    char *fish;
    long cur_day[9] = {0};

    fp = fopen("../inputs/day6.txt", "r");

    while (fgets(s, sizeof s, fp) != NULL)
    {
        fish = strtok(s, delim);
        do
        {
            cur_day[atoi(fish)] += 1;
        } while ((fish = strtok(NULL, delim)) != NULL);
    };

    for (int day = 0; day < 256; day++)
    {
        long zero = *cur_day;
        for (int d = 0; d < 8; d++)
        {
            cur_day[d] = cur_day[d + 1];
        }
        cur_day[8] = zero;
        cur_day[6] += zero;
    }

    long fish_count = 0;
    for (int i = 0; i < 9; i++)
    {
        fish_count += cur_day[i];
    }
    printf("after 256 days, there are %ld fish\n", fish_count);

    clock_t end = clock();
    time_spent += (double)(end - begin) / CLOCKS_PER_SEC;
    printf("Ran in %f seconds\n", time_spent);
}