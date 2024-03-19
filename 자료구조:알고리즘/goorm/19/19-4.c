#include <stdio.h>
int main()
{
    int N, i, age, sum;
    int min = 100;
    int max = 0;
    scanf("%d", &N);
    for(i=0; i<N; i++)
    {
        scanf("%d", &age);
        if(age>max)
        {
            max = age;
        }
        if(age<min)
        {
            min = age;
        }
    }
    sum = max - min;
    printf("%d", sum);
    return 0;
}