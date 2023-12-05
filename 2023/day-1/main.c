#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(void) {
    FILE *fp;
    char line[1024];
    int sum = 0;

    fp = fopen("input.txt", "r");

    while (fgets(line, sizeof(line), fp) != NULL) {
        line[strcspn(line, "\n")] = '\0';

        char *start = NULL;
        char *end = NULL;

        for (int i = 0; line[i] != '\0'; i++) {
            if (isdigit(line[i])) {
                if (start == NULL) {
                    start = &line[i];
                }
                end = &line[i];
            }
        }

        if (start != NULL && end != NULL) {
            char digit[3] = {start[0], end[0], '\0'};
            sum += atoi(digit);
        }
    }

    fclose(fp);

    printf("Part 1: %d\n", sum);
    return 0;
}
