/* This program demonstrates a function recieving a 2 dimensional array, summing its rows and stores it in a
1 dimensional array in the respective slots.
File: ex1_ws4.h
Author: Gal Elhiani
Tester: Amir Malul
*/

#include <stdio.h>                              //for printf
#include <stdlib.h>                             //for malloc() operations
#include "ex1_ws4.h"                            //header file containing SumOfRows() declaration

/*a function that returns a int* pointer of an array. recieves a 2 dimensional array as pointer to pointer int** arr
and its dimensions int rows & int cols
*/

int* SumOfRows(int **arr, int rows, int cols)
{
    int* sum =(int*) malloc(sizeof(int)* rows);         //allocate memory for the result array (one dimensional)
    if(sum == NULL)                                     //verify pointer integrity

    {
        return NULL;
    }
    
    //Nested for loops to summerize the rows and store them in sum
    
    for (int i = 0; i < rows; i++){
        int temp = 0;
        for (int j = 0; j < cols; j++)
        {
            temp+= arr[i][j];
        }
        sum[i] = temp;

    }
    return sum;
}

int main(void)
{
    int rows = 5;                                       //initialize 2 dimensional array's dimensions
    int cols = 5;
    int **array = (int **)malloc(rows * sizeof(int*));  //allocate memory for array rows using int* so we could point to columns
    for (int i = 0; i < rows; i++)
    {
        array[i] = (int *)malloc(cols * sizeof(int));   //allocate memory for colunms 
    }
    
    //For loop to print initialized 2 dimensional array for testing purposes
    
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            array[i][j] = i;
            printf("%d" , array[i][j]);
        }
        printf("\n");
    }

    int *processed = SumOfRows(array, rows, cols);      //initialize a pointer to point to SumOfRows function call
    
    //For loop to print the result array
    
    for (int i = 0; i < rows; i++)
    {

            printf("%d\t", processed[i]);          

    }
    free(processed);                                    //Free the pointer after finished using
    for (int i = 0; i < rows; i++)                      
    {
        free(array[i]);                                 //Free array columns memory
    }
    free(array);                                        //Free array rows memory

    return 0;
    
}