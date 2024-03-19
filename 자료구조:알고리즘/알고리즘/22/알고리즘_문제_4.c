#include <stdio.h>
int a[2][101];

int main() {
    int n, i, j;
    scanf("%d", &n);
    for(i=0; i<n; i++) {
        scanf("%d", &a[0][i]);
        a[1][i]=1;
    }
    for(i=0; i<n; i++) {
        for(j=0; j<n; j++) {
            if(a[0][i]<a[0][j])
        }
    }
}