#ifndef _STACK_H_
#define _STACK_H_
#include <stddef.h>


typedef struct Stack Stack;

Stack* Create(size_t element_size, size_t capacity);

void Destroy(Stack *stack);

void* Pop(Stack* stack);

void* Peek(const Stack* stack);

void Push(Stack *stack, void* element);

size_t Size(const Stack* stack);

int IsEmpty(const Stack* stack);

int Capacity(const Stack* stack);

#endif