#include <stdio.h>
#include <stdlib.h>

int main()
{
    int value;
    scanf("%d",&value);
    if(value<0)
        printf("negative");
    else if(value>0)
        printf("Positive");
    else
        printf("Zero");
return 0;
}
