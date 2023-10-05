#include <stdio.h>
 
int main() {
    double A;
    double B;
    double nota;
    scanf("%lf",&A);
    scanf("%lf",&B);
    nota = ((A*3.5)+(B*7.5))/11;

    printf("MEDIA = %.5lf\n",nota);
    
    return 0;
}