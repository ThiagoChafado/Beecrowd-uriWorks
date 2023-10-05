while True:
    N = int(input())
    if N ==0:
        break
    jogos = list(map(int,input().split()))
    maria = 0
    joao = 0
    for contador in jogos:
        if contador == 0:
            maria +=1
        else:
            joao +=1
    print(f'Mary won {maria} times and John won {joao} times')
    