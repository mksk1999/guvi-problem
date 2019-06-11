#include <stdio.h>
#include <stdlib.h>

int main()
{
    int value;
    scanf("%d",&value);
    if(value%2==0)
        printf("Even");
   // else if(value>0)
       // printf("Positive");
    else
        printf("Odd");
return 0;
}
