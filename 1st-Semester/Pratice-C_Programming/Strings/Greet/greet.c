#include <stdio.h>

int main() {
    char greetings[] = "Hello, World!";
    printf("%s\n", greetings);
    // Size of the greetings array
    printf("Size of greetings array: %d\n", sizeof(greetings));

    //Char by char printing
    printf("%c\n", greetings[0]);

    //String modification
    greetings[7] = '2';
    greetings[8] = 'C';
    printf("%s\n", greetings);
    return 0;
}