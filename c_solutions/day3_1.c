#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

int main(void)
{
    FILE *fp;
    char s[1024];
    int bit_count[12] = {0};
    char gamma[12] = {0};
    char epsilon[12] = {0};
    struct measurements {
        unsigned int gamma:12;
        unsigned int epsilon:12;
    };

    fp = fopen("../inputs/day3.txt", "r");

    while (fgets(s, sizeof s, fp) != NULL)
    {
        for (int i = 0; i < 12; i++)
        {
            if (s[i] == 48)
            {
                bit_count[i]--;
            }
            else
            {
                bit_count[i]++;
            }
        }
    }

    for (int j = 0; j < 12; j++)
    {
        if (bit_count[j] < 0)
        {
            gamma[j] = '0';
        }
        else
        {
            gamma[j] = '1';
        }
    }

    struct measurements results;
    printf("%s\n", gamma);
    results.gamma = strtol(gamma, NULL, 2);
    results.epsilon = ~results.gamma;
    printf("%d \n", results.gamma);
    printf("%d \n", results.epsilon);
    printf("%d \n", results.epsilon*results.gamma);

}