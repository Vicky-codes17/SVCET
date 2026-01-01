/*
 C program to perform XOR operation with 0 on each character of a 
 string and display the output.
*/
#include <stdio.h>

int main() {
    char *str = "Hello world";
    int i;

    for (i = 0; str[i] != '\0'; i++) {
        printf("%c", str[i] ^ 0);
    }

    return 0;
}
