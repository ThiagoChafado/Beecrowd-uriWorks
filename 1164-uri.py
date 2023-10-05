N = int(input())
for i in range(1,N+1):
    contador = 1
    soma = 0
    X = int(input())
    while contador < X:
        if (X%contador)==0:
            soma = soma + contador

        contador = contador +1
    if soma == X:
        print(f"{X} eh perfeito")
    else:
        print(f"{X} nao eh perfeito")

        

