/* This program demonstrates how to implement StrLen()

File: strlen.c
Author: Gal Elhiani
Tester: 
*/

#include <stdio.h>
#include <assert.h>
#include "string.h"


size_t StrLen(const char* str)
{
    assert(str);
    size_t count = 0;
    char c = *str;

    while(*str != '\0')
    {
        count++;
        str++;
        c = *str;

    }
    return count;
}

//main function for testing

int main(void)
{
    char* string = "Hello World";
    size_t x = StrLen(string);
    printf("%zu\n", x);
    
}
