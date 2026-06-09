/* This program demonstrates how to swap two integers using pointers in C.
File: ex1_ws2.c
Author: Gal Elhiani
Tester: Amir Gablinger
*/
#include <stdio.h>   //include the standard input/output library for printf function

void swap(int *a, int *b) 
{
    int temp = *a;
    *a = *b;
    *b = temp;
}


/*main function for testing*/
int main() 
{
    int x = 5;
    int y = 10;
    printf("before swap: x = %d, y = %d\n", x, y);
    swap(&x, &y);
    printf("after swap: x = %d, y = %d\n", x, y);
    return 0;
}