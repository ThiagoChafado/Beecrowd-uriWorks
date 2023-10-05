#include <stdio.h>

int fatorial(a){
    if (a==0){
        return 1;
    }return a*fatorial(a-1);
}

int main() {
    int N;
    scanf("%d",&N);
    printf("%d\n",fatorial(N));
    return 0;
}