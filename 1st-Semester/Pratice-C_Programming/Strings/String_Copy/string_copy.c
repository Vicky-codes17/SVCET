#include <stdio.h>
#include <string.h>

int main() {
    char str1[20] = "Hello";
    char str2[20] = "hello";

    strcpy(str2, str1);

    //Compare
    strcmp(str1, str2);
    printf("%d\n", strcmp(str1, str2)); // 0 if equal

    printf("Source String: %s\n", str1);
    printf("Destination String after copy: %s\n", str2);

    return 0;
}

//mrmory address