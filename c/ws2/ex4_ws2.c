/* This program demonstrates how to print a char pointer.
File: ex4_ws2.c
Author: Gal Elhiani
Tester: Amir Gablinger
*/

#include <stdio.h>

char c = 'c';
char* pointer = &c;

int main(void)
{
    printf("%p\n", pointer);
}