#include <stdio.h>
#define swap(x,y,t) ((t)=(x), (x)=(y), (y)=(t))
int n, cnt;
int partition(int list[], int left, int right)
{
    int pivot, low, high,temp;
    low=left;
    high=right+1;
    pivot=list[left];
    do{
        do{
            low++;
        }while(pivot<list[low]);
        do{
            high--;
        }while(pivot>list[high]);
        if(low<high)
        {
            swap(list[low], list[high], temp);
        /*   temp=list[low];
            list[low]=list[high];
            list[high]=temp;*/
        }
    }while(low<high);
    swap(list[high], list[left], temp);
    /*temp=list[high];
    list[high]=list[left];
    list[left]=temp;*/
    return high;
}

void quicksort(int list[], int left, int right)
{
    if(left<right)
    {
        int q=partition(list,left,right);
        printf("%d단계: ", ++cnt);
        for(int i=0;i<n;i++)
        {
            printf("%d ",list[i]);
        }   
        printf("\n");
        quicksort(list,left,q-1);
        quicksort(list,q+1,right);
    }
}

int main()
{
    int list[65];
    int i;
    scanf("%d", &n);
    for(i=0;i<n;i++)
        scanf("%d",&list[i]);
    quicksort(list,0,n-1);

    return 0;
}