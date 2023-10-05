#include <stdio.h>
#include <stdlib.h>
 
int main() {
    int alcool=0,gasolina=0,diesel=0,i,combustivel=0;
    while (combustivel!=4){
        scanf("%d",&combustivel);
        if(combustivel==1){
            alcool=alcool+1;
        }if(combustivel==2){
            gasolina =gasolina+1;
        }if (combustivel==3){
            diesel=diesel+1;
        }if (combustivel<1 ||combustivel>4){
            combustivel=0;
        }
    }printf("MUITO OBRIGADO\n");
    printf("Alcool: %d\n",alcool);
    printf("Gasolina: %d\n",gasolina);
    printf("Diesel: %d\n",diesel);
    
    return 0;
}