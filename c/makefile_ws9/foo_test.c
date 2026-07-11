#include <stdio.h>
#include "foo.h"



int main(void)
{
    int x = 1;
    Add(&x);
    printf("%d", x);
    return 0;
}
