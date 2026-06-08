/* This program defines a function to reverse the digits of an integer and includes a main function for testing.
File: ex5.c
Author: Gal Elhiani
Tester: Viktoria Tyshchenko
 */
#include <stdio.h>

int reverse(int n) 
{
    int reversed = 0;
    int digit = 0;
    int abs_n = n < 0 ? -n : n;
    while (n > 0)
    {
        digit = n%10;
        n/=10;
        reversed+=digit;
        reversed*=10;
    }
    reversed /=10;
    if (n < 0) 
    {
        reversed = -reversed;
    }
    return reversed;
}
/*main function for testing*/
int main() 
{
    int number = 123450;
    printf("Original number: %d\n", number);
    printf("Reversed number: %d\n", reverse(number));
    return 0;
}