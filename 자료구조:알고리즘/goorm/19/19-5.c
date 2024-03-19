#include <stdio.h>
int main()
{
    char num[100];
    int i;
    scanf("%s", num);
    if(num[7]==1 || num[7]==3)
    {
        char gender = 'M';
    }
    else
    {
        char gender = 'W';
    }
    printf("%c", gender);
    
    return 0;
}