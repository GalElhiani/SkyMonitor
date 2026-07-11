/* This program lists and prints all of environmental variables into char** buffer
in lower case.

File: ex4_ws4.c
Author: Gal Elhiani
Tester: Amir Malul
*/

#include <stdio.h>              //for printf
#include <stdlib.h>             //for access to malloc
#include <string.h>             //for access to strlen
#include <assert.h>             //for access to assert (working with pointers)

extern char **environ;          //initialize a global buffer

int main() {
    int count = 0;

    //while loop to count the variables in the environment
    while (environ[count] != NULL) {
        count++;
    }

    //allocate the outer pointer array and assert to check
    char **env_copy = (char **)malloc((count + 1) * sizeof(char *));
    assert(env_copy != NULL);

    //for loop that allocates memory to env_copy, copies the variable and converts to lowercase
    for (int i = 0; i < count; i++) {
        
        size_t length = strlen(environ[i]);                                 //check current variable length
        env_copy[i] = (char *)malloc((length + 1) * sizeof(char));          //allocate memory for string + '\0'
        assert(env_copy[i] != NULL);

        //for loop to copy all the chars
        for (size_t j = 0; j < length; j++) {
            char c = environ[i][j];
            
            //if statement to check if a char is upper case, if it is we change it to lowercase
            if (c >= 'A' && c <= 'Z') {
                env_copy[i][j] = c + 32;                                   //use ASCII index to convert it to lowercase
            } else {
                env_copy[i][j] = c;                                        //keep numbers and symbols unchanged
            }
        }

        
        env_copy[i][length] = '\0';                                        //insert string terminator
    }

    env_copy[count] = NULL;                                                //put a stop condition to the loop by inserting NULL at the end

    //for loop to print the char**
    for (int i = 0; env_copy[i] != NULL; i++) {
        printf("%s\n", env_copy[i]);
    }

    //for loop to free the memory
    for (int i = 0; i < count; i++) {
        free(env_copy[i]);
    }
    free(env_copy);

    return 0;
}