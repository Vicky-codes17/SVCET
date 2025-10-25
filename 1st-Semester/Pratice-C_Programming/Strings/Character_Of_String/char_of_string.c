#include <stdio.h>

int main() {
    char greeting[] = "Hello, World!";
    for ( int i = 0; i<13; i++) {
        printf("Index of %d: %c\n", i, greeting[i]);
    }
    return 0;
}