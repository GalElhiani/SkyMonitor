/* This program demonstrates a solution for the Josephus Problem
File: ex2_ws4.c
Author: Gal Elhiani
Tester: Amir Malul
*/

#include <stdio.h>                                          //include for printf usage
#include <stdbool.h>                                        //include for boolean operations

//A function that calcultes the josephus problem:
    int JosephusProblemSolver(int* array, int size)
    {
        int index = 0;                                      //initialize an index to move through array
        int last_alive_index = 0;                           //last_alive_index to store the index of the last survivor
        bool skip_next = true;                              //a boolean flag to mark if we need to skip a solider or kill him
        int alive_counter = size;                           //a variable to store the remaining amonut of alive soldiers
        while(alive_counter > 1)                            //it will be used as an exit condition for the while loop
        {
            index = (index+1) % size;                       //this operation lets us circle back the array using modulu
            if(array[index] != -1)                          //if soldier is alive (-1) marks a dead soldier
            {
                if(skip_next)                               
                {
                    last_alive_index = index;               //update the last alive index
                    skip_next = false;
                }
                else
                {
                    array[index] = -1;                      //if we dont skip the soldier, we "kill" him
                    alive_counter--;                        //update the alive counter
                    skip_next = true;                       //we will skip the next in line
                    
                }
            }


            
        }
        return last_alive_index;
        
    }

int main(int argc, char const *argv[])
{
    int array[100];
    int size = 100;


    for (int i = 0; i < size; i++)
    {
        array[i] = i;        
    }
    

    int winner =   JosephusProblemSolver(array, size);
    printf("%d\n", winner);
    return 0;

}
