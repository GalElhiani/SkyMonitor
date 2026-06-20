#include <stdio.h>
#include "g.h"

int g_s = 3;

int main(void)
{
    (void)printf("Initial g_s: %d\n", g_s);
    
    Foo();
    
    (void)printf("Post-Foo g_s: %d\n", g_s);
    
    return 0; 
}