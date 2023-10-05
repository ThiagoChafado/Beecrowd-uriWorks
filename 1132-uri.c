#include <stdio.h>
#include <stdlib.h>
 
int main() {
    int x,y,i,soma=0;
    scanf("%d",&x);
    printf("");
    scanf("%d",&y);
    printf("");
    if (x<y){
        for(i=x;i<y+1;i++){
            if (i%13!=0){
                soma = soma +i;
            }
        }printf("%d\n",soma);
    }else if(x>y){
        for (i=y;i<x+1;i++){
            if(i % 13 != 0){
                soma=soma+i;
            }
        }printf("%d\n",soma);
    }

    
    

    

    return 0;
}