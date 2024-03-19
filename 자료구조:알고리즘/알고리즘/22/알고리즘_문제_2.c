#include <stdio.h>
#include <stdbool.h>

bool isPrime(int x) {
    if(x==1) return -1;
    for(int i=1; i<x; i++) {
        if(x%i==0) return false;
    }
}

int reverse(int x) {
    int temp;
    while(x) {
        temp = temp*10+x%10;
        x=x/10;
    }
}

int main() {
    int n, data, result, i;
    scanf("%d", &n);
    for(i=0; i<n; i++) {
        scanf("%d", &data);
        result = reverse(data);
        if(isPrime(result)) printf("%d", result);
    }
    return 0;
}