/*To write a C program to perform bitwise AND, OR, and XOR operations
 with 127 on each character of a string and display the output.*/

 #include <stdio.h>

int main() {
    char *str = "HelloWorld";
    int i;

    printf("AND with 127:\n");
    for (i = 0; str[i] != '\0'; i++) {
        printf("%c", str[i] & 127);
    }

    printf("\n\nOR with 127:\n");
    for (i = 0; str[i] != '\0'; i++) {
        printf("%c", str[i] | 127);
    }

    printf("\n\nXOR with 127:\n");
    for (i = 0; str[i] != '\0'; i++) {
        printf("%c", str[i] ^ 127);
    }

    return 0;
}
