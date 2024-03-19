#include <stdio.h>

int main() {
    char a[101];
    int b[10];
    int i, max, index;
    scanf("%s", a);
    for(i=0; a[i]!='\0'; i++) {
        b[a[i]-'0']++;
    }
    for(i=0; i<10; i++) {
        if(b[i]>=max) {
            max=b[i];
            index=i;
        }
    printf("%d", index);
    return 0;
    }
}