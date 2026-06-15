#include "stack.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <assert.h>

struct Stack 
{
    void* data;
    size_t element_size;
    size_t size;
    size_t capacity;
    void* last_element;    
};


Stack* Create(size_t element_size, size_t capacity)
{
    Stack* stack = malloc(sizeof(Stack));
    assert(stack);

    stack->data = malloc(element_size*capacity);
    if(stack->data == NULL)
    {
        return NULL;
    }
    stack->element_size = element_size;
    stack->capacity = capacity;
    stack->size = 0;
    return stack;

}

int IsEmpty(const Stack* stack)
{
    assert(stack);
    return stack->size == 0;
}

void Destroy(Stack *stack)
{
    free(stack->data);
    free(stack);
}

void* Pop(Stack* stack)
{   
    void* temp;
    char* last_address;
    assert(stack);

    if(IsEmpty(stack))
    {
        printf("Error: cannot perform pop on an empty stack!");
        return 0;
    }
    stack->size--;

    temp = malloc(stack->element_size);

    last_address = (char*)stack->data+(stack->size*stack->element_size);
    memcpy(temp, last_address, stack->element_size);
    return temp;

}

void Push(Stack* stack, void* element)
{
    char* last_address;
    assert(stack); 
    if(stack->size == stack->capacity)
    {
        return;
    }
    stack->size++;
    last_address = (char*)stack->data+((stack->size-1)*stack->element_size);
    memcpy(last_address, element, stack->element_size);

}

void* Peek(const Stack* stack)
{
    assert(stack);
    return (void*)((char*)stack->data +(stack->size*stack->element_size));
}

size_t Size(const Stack* stack)
{
    assert(stack);
    return stack->size;
}


int Capacity(const Stack* stack)
{
    assert(stack);
    return stack->capacity;
}