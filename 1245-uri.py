while True:
    try:
        N=int(input())
        if N==0:
            break
        pares = 0
        sapatos = [0 for c in range(61)]
        for i in range(N):
            M,L=input().split(' ')
            M=int(M)
            if(L == 'D'):
                if(sapatos[M] < 0):
                    pares += 1
                sapatos[M] += 1
            else:
                if(sapatos[M] > 0):
                    pares += 1
                sapatos[M] -= 1
        print(pares)
    except EOFError:
        break
        
