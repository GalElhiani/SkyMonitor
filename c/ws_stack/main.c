/*This program demonstrates the implementation of stack data structure
and its functions to manipulate it.
File: main.c
Author: Gal Elhiani
Tester: Nehorai
to run the test on this program use make and then ./result in the console
 
*/


/***************************** VLG REPORT *****************************/
/*
==71087== Memcheck, a memory error detector
==71087== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==71087== Using Valgrind-3.18.1 and LibVEX; rerun with -h for copyright info
==71087== Command: ./result
==71087== 
create test passed
isempty test passed
capacity test passed
push test passed
size test passed
peek test passed
pop test passed
destroy test passed
==71087== 
==71087== HEAP SUMMARY:
==71087==     in use at exit: 0 bytes in 0 blocks
==71087==   total heap usage: 3 allocs, 3 frees, 1,080 bytes allocated
==71087== 
==71087== All heap blocks were freed -- no leaks are possible
==71087== 
==71087== For lists of detected and suppressed errors, rerun with: -s
==71087== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
*/
/***********************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include "stack.h"

int main()
{
    Stack* stack;
    int n1;
    int n2;
    int n3;
    int* peeked;
    int* popped;
    size_t size_result;
    int empty_result;
    int cap_result;

    n1 = 10;
    n2 = 20;
    n3 = 30;

    stack = Create(sizeof(int), 3);
    if (stack == NULL) {
        printf("create test failed\n");
        return 1;
    }
    printf("create test passed\n");

    empty_result = IsEmpty(stack);
    if (empty_result != 1) {
        printf("isempty test failed\n");
        Destroy(stack);
        return 1;
    }
    printf("isempty test passed\n");

    cap_result = Capacity(stack);
    if (cap_result != 3) {
        printf("capacity test failed\n");
        Destroy(stack);
        return 1;
    }
    printf("capacity test passed\n");

    Push(stack, &n1);
    Push(stack, &n2);
    Push(stack, &n3);
    printf("push test passed\n");

    size_result = Size(stack);
    if (size_result != 3) {
        printf("size test failed\n");
        Destroy(stack);
        return 1;
    }
    printf("size test passed\n");

    peeked = (int*)Peek(stack);
    if (peeked == NULL || *peeked != 30) {
        printf("peek test failed\n");
        Destroy(stack);
        return 1;
    }
    printf("peek test passed\n");

    popped = (int*)Pop(stack);
    if (popped == NULL || *popped != 30) {
        printf("pop test failed\n");
        Destroy(stack);
        return 1;
    }
    printf("pop test passed\n");
    free(popped);

    Destroy(stack);
    printf("destroy test passed\n");

    return 0;
}