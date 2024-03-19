#include <stdio.h>
int i,k,n=8;
int hash(int key)
{
    return key%n;
}
int main()
{
    int key;
    int list[8]={0,0,10,3,2,5,0,0};
    scanf("%d",&key);
    int index=hash(key);
    int t = index;
    while(1)
    {
        if(list[index]==0)
        {
            list[index]=key;
            break;
        }
        else
        {
            k++;
            index=(hash(key)+k)%n;
            if(t==index){
                printf("탐색 실패");
                break;
            } 
        }
    }
    printf("%d",index);
    return 0;
}