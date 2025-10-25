#include <stdio.h>
#include <string.h>
int main() {
    char name[30] = "Hi I AM VIGNESH";
    printf("Length is : %lu\n", strlen(name));
    printf("Size is : %lu\n", sizeof(name));

    printf("Size is : %zu\n", sizeof(name));

    printf("Length is : %d\n", strlen(name));
    return 0;
}