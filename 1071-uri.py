X = int(input())
Y = int(input())
soma = 0
for contador in range(X-1,Y,-1):
    if (contador%2==1):
        soma = soma + contador
print(soma)