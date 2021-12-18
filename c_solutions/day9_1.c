#include <stdio.h>
#include <stdlib.h>

struct Node {
    int height;
    struct Node *neighbors;
};

int get_neighbors(int map[], int x, int y) {
    return;
}

char* get_location(int x, int y) {
    return;
}

int main(void)
{
    FILE *fp;
    char s[104];
    char c;
    int map[100][100];
    int row_count = 0;
    int col_count = 0;

    fp = fopen("../inputs/day9.txt", "r");

    while (fgets(s, sizeof s, fp) != NULL)
    {
        col_count = 0;
        while ((c = s[col_count]) != '\n')
        {
            map[row_count][col_count] = c - '0';
            col_count += 1;
        }
        row_count += 1;
    }

    for (int i = 0; i < row_count; i++)
    {
        for (int j = 0; j < col_count; j++)
        {
            printf("%d", map[i][j]);
        }
        printf("\n");
    }
}