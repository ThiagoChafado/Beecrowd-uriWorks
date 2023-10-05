#include <stdio.h>
#include <stdlib.h>
 
int main() {
    int x=1,i;
    while (x!=0){
        scanf("%d",&x);
        for(i=1;i<x+1;i++){
            if (i!=x){
            printf("%d ",i);
            }else{
                printf("%d\n",i);
            }
        }
    }

    return 0;
}   