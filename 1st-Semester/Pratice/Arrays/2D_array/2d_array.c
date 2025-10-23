#include <stdio.h>

int main() {
    int a[2][3] = {{1, 2, 3}, {4, 5, 6}};

    printf("Elements of 2D array are:\n");
    // First ROW
    printf("%d", a[0][0]);
    printf("\n%d", a[0][1]);
    printf("\n%d", a[0][2]);
    // Second ROW
    printf("\n%d", a[1][0]);
    printf("\n%d", a[1][1]);
    printf("\n%d\n", a[1][2]);
}