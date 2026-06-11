/* This program demonstrates the following:
1) how a function recieves a two dimensional array in several ways.
2) it also acts a header file for ex1_ws4.c
File: ex1_ws4.h
Author: Gal Elhiani
Tester: Amir Malul
*/
#ifndef _EX1_H_
#define _EX1_H_
//a function signature that recieves two dimensional arrays in several ways:

//a) writing an interface for the functions:

void RecieveArray1(int rows, int columns ,int arr[rows][columns]);     //- as 2D array
void RecieveArray2(int rows, int cols,int (*array)[cols]);      //-  as pointer to array
int* SumOfRows(int **arr, int rows, int cols);        //-  as single level pointer

#endif

/*b) to access a specific location (n) in an array:
int array[10] = (1,2,3,4,5,6,7,8,9);
int n = 5;
int x = array[n];
printf("%d", n);

output: 5
*/

/*c) to check sizeof an array we'll use:
    size_t size = sizeof(array);

    depending on the type of the array, the sizeof will return different number
    according to the specific datatype the array is initialized because different
    data types occupy different amount of space. which may also vary based on the
    operating system this code is ran on.
    on this specific system and a specific type of int array
    size = 40, because an integer is 4 bytes and is 10 long so 10*4 = 10;


*/
