#include "partOne.h"

void partOne(const char *filename) {
    FILE* fp = fopen(filename, "r");
    char ch, start = 0, end = 0;
    int sum = 0;
    while(1) {
        ch = fgetc(fp);
        if(feof(fp))
            break;
        if(ch != '\n') {
            if(isdigit(ch)) {
                if (start == '\0')
                    start = ch;
                end=ch;
            }
        } else {
            char n[] = {start, end, '\0'};
            sum+=atoi(n);
            start = end = '\0';
        }
        continue;
    }
    fclose(fp);
    printf("Sum of calibration values: %d\n", sum);
}
