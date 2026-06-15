#include <stdio.h>
#include <stdlib.h>
#include "stack.h"

int main()
{
    Stack* stack;
    int n1;
    int n2;
    int n3;
    int n4;
    int* peeked;
    int* popped;
    int* empty_pop;

    n1 = 10;
    n2 = 20;
    n3 = 30;
    n4 = 40;

    stack = Create(sizeof(int), 3);
    if (!stack) return 1;

    printf("is_empty: %d, size: %lu, capacity: %d\n", 
           IsEmpty(stack), Size(stack), Capacity(stack));

    Push(stack, &n1);
    Push(stack, &n2);
    Push(stack, &n3);

    printf("is_empty: %d, size: %lu, capacity: %d\n", 
           IsEmpty(stack), Size(stack), Capacity(stack));

    Push(stack, &n4);

    peeked = (int*)Peek(stack);
    if (peeked) {
        printf("peeked: %d\n", *peeked);
    }

    while (!IsEmpty(stack)) {
        popped = (int*)Pop(stack);
        if (popped) {
            printf("popped: %d\n", *popped);
            free(popped);
        }
    }

    printf("post-pop - is_empty: %d, size: %lu\n", IsEmpty(stack), Size(stack));

    empty_pop = (int*)Pop(stack);
    free(empty_pop);

    Destroy(stack);
    return 0;
}