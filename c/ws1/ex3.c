/* This program prints "Hello World!" using hexadecimal escape sequences.
File: ex3.c
Author: Gal Elhiani
Tester: Viktoria Tyshchenko
*/
#include <stdio.h>  //include the standard input/output library for printf function

int main() {
    printf("\x22\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21\x22\x0a");
    return 0;
}