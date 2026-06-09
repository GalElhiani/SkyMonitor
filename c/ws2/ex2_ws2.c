/* This program demonstrates how to copy an array to an existing array.
File: ex1_ws2.c
Author: Gal Elhiani
Tester: Amir Gablinger
*/

#include <stdio.h>
#include <assert.h>

void ArrayCopy(int* arr_ptr1, int* arr_ptr2, int size_of_arr1)
{
    assert(arr_ptr1);
    assert(arr_ptr2);
    assert(size_of_arr1 > 0);

    for(int i = 0; i < size_of_arr1; i++){
        *(arr_ptr2 + i) = *(arr_ptr1 + i);
    }
}


/*main function for testing*/

int main(void)
{
    int array1[] = {1,2,3,4,5};
    int arr_size = sizeof(array1) / sizeof(array1[0]);
    int array2[arr_size];
    ArrayCopy(array1, array2, arr_size);
    for(int i = 0; i < arr_size; i++)
    {
        printf("%d", array2[i]);
    }
    printf("\n");
}