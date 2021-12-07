#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>


struct node {
        unsigned long value:12;
        struct node *next;
    };
struct measurements {
        unsigned int co2:12;
        unsigned int oxy:12;
    };
int create_linked_list(struct node, FILE *fp) {
    char s[1024];
    while (fgets(s, sizeof s, fp) != NULL)
    {
        node.value = strtol(s, NULL, 2); 
    }
}

int main(void)
{
    FILE *fp;
    char s[1024];
    int count = 0;
    int ptr = 0;

    fp = fopen("../inputs/day3.txt", "r");

    struct node head;
    head.value = strtol(s, NULL, 2);

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
    results.gamma = strtol(gamma, NULL, 2);
    results.epsilon = ~results.gamma;
    printf("%d \n", results.gamma);
    printf("%d \n", results.epsilon);
    printf("%d \n", results.epsilon*results.gamma);

}