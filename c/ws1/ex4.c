/* This program defines a function PowerOfTen that calculates 10 raised to the power of n. 
   It handles both positive and negative values of n, as well as the case when n is zero. 
   The main function tests the PowerOfTen function with different values of n and prints the results.
File: ex4.c
Author: Gal Elhiani
Tester: Viktoria Tyshchenko 
*/

#include <stdio.h>

double PowerOfTen(int n) 
{
    double result = 1;
    if (n == 0) 
    {
        return result; // 10^0 is 1
    }
    int abs_n = n < 0 ? -n : n; 
    for (int i = 0; i < abs_n; i++) 
    {
        result *= 10;
    }
    if (n < 0) 
    {
        result = 1.0 / result;
    }
    return result;
}
/*main function for testing*/
int main() 
{
    printf("%f\n", PowerOfTen(3));
    printf("%f\n", PowerOfTen(-2));
    printf("%f\n", PowerOfTen(0));
    return 0;
}