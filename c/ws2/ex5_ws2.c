/* This program demonstrates how to impplement swapping size_t variables.
and size_t pointers, and eventually implementing swapping of size_t pointers
with the first function.

File: ex5_ws2.c
Author: Gal Elhiani
Tester: Amir Gablinger
*/

#include <stdio.h>

void SwapTwoSizeT(size_t* a, size_t* b)
{
    size_t temp = *a;
    *a = *b;
    *b = temp;
}

void SwapTwoPointers(size_t** ptr1, size_t** ptr2)
{
    size_t* temp = *ptr1;
    *ptr1 = *ptr2;
    *ptr2 = temp;
}

void NestedSwap(size_t** ptr1, size_t** ptr2)
{
    SwapTwoSizeT((size_t*)ptr1,(size_t*) ptr2);
}



int main(void)
{
    size_t size1 = 4;
    size_t size2 = 9;
    size_t* pointer1 = &size1;
    size_t* pointer2 = &size2;
    printf("Before Swap: \n");
    printf("%zu\n", size1);
    printf("%zu\n", size2);

    printf("%p\n", pointer1);
    printf("%p\n", pointer2);


    SwapTwoSizeT(&size1, &size2);
    SwapTwoPointers(&pointer1, &pointer2);

    printf("After Swap: \n");

    printf("%zu\n", size1);
    printf("%zu\n", size2);


    printf("%p\n", pointer1);
    printf("%p\n", pointer2);

    printf("After Nested swap: \n");

    NestedSwap(&pointer1, &pointer2);

    printf("%p\n", pointer1);
    printf("%p\n", pointer2);
}