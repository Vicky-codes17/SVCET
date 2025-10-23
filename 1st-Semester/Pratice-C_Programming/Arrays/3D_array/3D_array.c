#include <stdio.h>

int main() {
    int a[2][4][3] = {
        {{1, 2, 3},{4, 5, 6},{7, 8, 9},{10, 11, 12}},
        {{13, 14, 15},{16, 17, 18},{19, 20, 21},{22, 23, 24}}
    };

    //Size of 3D array
    printf("Size of 3D array: %d\n", sizeof(a));

    //Looping
    for(int i=0;i<2;i++) {
        printf("Layer %d:\n", i+1);
        for (int j=0;j<4;j++) {
            for(int k=0;k<3;k++) {
                printf("%d ", a[i][j][k]);
            }
            printf("\n");
        }
        printf("\n");
    }
}