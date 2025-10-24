#include <stdio.h>

int main() {
    char greetings[] = "Hello, World!";
    printf("%s\n", greetings);
    // Size of the greetings array
    printf("Size of greetings array: %d\n", sizeof(greetings));

    //Char by char printing
    printf("%c\n", greetings[0]);
    return 0;
}