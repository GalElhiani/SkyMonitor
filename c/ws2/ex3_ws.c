/* This program prints the addresses of several pointers.
File: ex3_ws2.c
Author: Gal Elhiani
Tester: Amir Gablinger
*/
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    static int s_i = 7;
    int* ptr = &s_i;
    int i = 7;
    int* ptr2 = &i;
    int** ptr3 = &ptr2;
    int* ptr4= (int *)malloc(sizeof(int));
    free (ptr4);

    printf("%p\n", ptr);
    printf("%p\n", ptr2);
    printf("%p\n", ptr3);
    printf("%p\n", ptr4);

    return 0;
}