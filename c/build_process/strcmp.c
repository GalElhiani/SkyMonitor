/* This program demonstrates how to implement StrCmp()

File: strlen.c
Author: Gal Elhiani
Tester: 
*/


#include <stdio.h>
#include <assert.h>
#include "string.h"

int StrCmp(const char *s1, const char *s2)
{
    assert(s1);
    assert(s2);
    char c1 = *s1;
    char c2 = *s2;
    while(c1 != '\0' || c2 != '\0')
    {
        if(c1 < c2)
        {
            return -1;
        }
        else if(c1 > c2)
        {
            return 1;
        }

        s1++;
        s2++;
        c1 = *s1;
        c2 = *s2;
    
    }

return 0;
}
  
int main(void)
{
    char* str1 = "ABC";
    char* str2 = "AB";

    int test = StrCmp(str1, str2);
    printf("%d\n", test);
    return 0;
}