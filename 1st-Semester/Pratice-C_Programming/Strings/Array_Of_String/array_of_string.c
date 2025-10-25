#include <stdio.h>

int main() {
    char greet[] = {'H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!'};
    printf("%s\n", greet);

    //Escape Characters
    char str[] = "Hello I am Vignesh,This is \"C Programming Practice\".";
    printf("%s\n", str);

    char slash[] = "This Text is for the \\ Backslash character.";
    printf("%s\n", slash);
    return 0;
}