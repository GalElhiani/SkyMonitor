#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *arr = malloc(10 * sizeof(int));
    for (int i = 0; i<10; i++)
    {
        arr[i] = i;
    }

    int x = arr[11];
}