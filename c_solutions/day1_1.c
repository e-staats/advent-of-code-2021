#include <stdio.h>
#include <stdlib.h>

int main(void) {
    
    char s[1024];
    FILE *fp;
    fp = fopen("../inputs/day1.txt", "r");
    int count = 0;
    int linecount = 0;
    unsigned long int depth1;
    unsigned long int depth2;
    
    depth1 = strtoul(fgets(s, sizeof s, fp), NULL, 10);
    while (fgets(s, sizeof s, fp) != NULL) {
        depth2 = strtoul(s, NULL, 10);
        printf("%d: %ld", ++linecount, depth2);
        if (depth2 > depth1) { count++; printf("    bigger");}
        printf("\n");
        depth1 = depth2;
    }

    fclose(fp);
    printf("count: %d", count);
}

