#include <stdio.h>

int main() {
    int arr[] = {10, 20, 30, 40, 50};
    float farr[] = {1.1, 2.2, 3.3, 4.4, 5.5};

    double barr2[] = {100.5, 200.5, 300.5, 400.5, 500.5};

    char carr[] = {'a', 'b', 'c', 'd', 'e', '1'};

    // arr[6] = 60;
    printf("\nArray elements are:\n");
    printf("%d\n",arr[0]);
    printf("%d\n",sizeof(arr[2]));

    // For the Float array
    printf("%d\n",sizeof(farr[2]));
    // For the Double array
    printf("%d\n",sizeof(barr2[2]));

    // For the Char array
    printf("%d\n",sizeof(carr[2]));


    return 0;
}