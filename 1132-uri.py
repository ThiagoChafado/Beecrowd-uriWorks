X = int(input())
Y = int(input())
soma = 0
if X < Y:
    for contador in range(X,Y+1,1):
        if (contador%13 != 0):
            soma = soma + contador
    print(soma)
else:
    for contador in range(X,Y-1,-1):
        if (contador%13 != 0):
            soma = soma + contador
    print(soma)