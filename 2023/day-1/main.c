#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(void) {
    FILE *fp;
    char ch, start = 0, end = 0;
    int sum = 0;
    
    fp = fopen("input.txt", "r");

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

    return 0;
}
