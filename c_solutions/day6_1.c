#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>       // for time()

int main(void)
{

    double time_spent = 0.0;
    clock_t begin = clock();

    FILE *fp;
    char s[1024];
    char delim[] = ",";
    char *fish;
    int starting_size = 400;
    int *cur_day = malloc(starting_size * sizeof(int));
    long cur_day_size = 0;
    int *next_day = malloc(starting_size * sizeof(int));
    long next_day_size = 0;
    long next_day_max = starting_size;

    fp = fopen("../inputs/day6.txt", "r");

    if (cur_day == NULL)
    {
        printf("Error allocating 200 ints\n");
        exit(500);
    }

    while (fgets(s, sizeof s, fp) != NULL)
    {
        fish = strtok(s, delim);
        do
        {
            *(cur_day + cur_day_size) = atoi(fish);
            cur_day_size++;
        } while ((fish = strtok(NULL, delim)) != NULL);
    };

    for (int day = 0; day < 80; day++)
    {

        printf("day %d, cur day size is %ld\n", day, cur_day_size);
        for (int f = 0; f < cur_day_size; f++)
        {
            //resize next_day if we don't have enough space:
            if (next_day_max - next_day_size < 3)
            {
                int *resize = realloc(next_day, sizeof(int) * next_day_max * 2);
                if (resize == NULL)
                {
                    printf("Error reallocating at size %ld\n", next_day_max * 2);
                    exit(1);
                }
                next_day = resize;
                next_day_max *= 2;
            }

            //meat of the logic:
            if (*(cur_day + f) == 0)
            {
                *(next_day + next_day_size) = 6;
                next_day_size++;
                *(next_day + next_day_size) = 8;
                next_day_size++;
            }
            else
            {
                *(next_day + next_day_size) = *(cur_day + f) - 1;
                next_day_size++;
            }
        }
        //prepare for next day:
        // for (int a = 0; a < cur_day_size; a++)
        // {
        //     printf("%d,", *(cur_day + a));
        // }
        // printf("\n");
        // for (int a = 0; a < next_day_size; a++)
        // {
        //     printf("%d,", *(next_day + a));
        // }
        // printf("\n");
        cur_day = next_day;
        cur_day_size = next_day_size;
        int *new_day = malloc(sizeof(int) * next_day_max);
        if (new_day == NULL)
        {
            printf("Error reallocating at size %ld\n", next_day_max);
            exit(1);
        }
        next_day = new_day;
        next_day_size = 0;
    }

    free(cur_day);
    free(next_day);
    printf("after 80 days, there are %ld fish\n", cur_day_size);

    clock_t end = clock();
    time_spent += (double)(end - begin) / CLOCKS_PER_SEC;
    printf("Ran in %f seconds\n", time_spent);
}