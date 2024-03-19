#include <stdio.h>

int main() {
    int n, m, data, cnt = 0, i, max = -1;
    scanf("%d %d", &n, &n);
    for(i=0; i<n; i++) {
        scanf("%d", &data);
        if(data>m) cnt++;
        else {
            if(cnt>max) max=cnt;
            cnt=0;
        }
    }
}