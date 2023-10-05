#include <stdio.h>
 
int main() {
    int a,b,n1,n2;
    float preco1,preco2,valor;

    scanf("%d %d %f",&a,&n1,&preco1);
    scanf("%d %d %f",&b,&n2,&preco2);
    valor = n1*preco1+n2*preco2;
    printf("VALOR A PAGAR: R$ %.2f\n",valor);

    
    return 0;
}