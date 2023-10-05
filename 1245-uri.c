#include <string.h>
#include <stdio.h>

int main(){
    char L;
    int sapatos[61];
    int N, M, pares;

    while(scanf("%d", &N) != EOF){
        pares = 0;
        memset(sapatos, 0, sizeof(sapatos));

        for(int i = 0; i < N; ++i){
            scanf("%d %c\n", &M, &L);

            if(L == 'D'){
                if(sapatos[M] < 0)  ++pares;
                ++sapatos[M];
            }else{
                if(sapatos[M] > 0)  ++pares;
                --sapatos[M];
            }
        }

        printf("%d\n", pares);
    }

    return 0;
}