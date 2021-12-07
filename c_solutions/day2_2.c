#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{

    FILE *fp;
    char s[1024];
    char delim[] = " ";
    char *ptr;
    char *command1;
    char *command2;
    long distance;
    long x = 0;
    long y = 0;
    long aim = 0;

    fp = fopen("../inputs/day2.txt", "r");

    while (fgets(s, sizeof s, fp) != NULL)
    {
        command1 = strtok(s, delim);    //first piece
        command2 = strtok(NULL, delim); //second piece;
        distance = strtol(command2, NULL, 10);
        if (strcmp(command1, "forward") == 0)
        {
            x += distance;
            y += distance*aim;
        }
        else if (strcmp(command1, "down") == 0)
        {
            aim += distance;
        }
        else if (strcmp(command1, "up") == 0)
        {
            aim -= distance;
        }
        printf("command1: %s command2: %ld  x: %ld y: %ld\n", command1, distance, x, y);
    }

    printf("x: %ld y: %ld  answer: %ld", x, y, x * y);
    fclose(fp);
}