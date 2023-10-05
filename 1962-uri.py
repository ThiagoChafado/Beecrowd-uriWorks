N = int(input())
for c in range(0,N):
    T = int(input())
    diferenca = T - 2015
    if diferenca < 0:
        diferenca = diferenca *(-1)
        print(diferenca,"D.C.")
    elif diferenca >= 0:
        diferenca = diferenca +1
        print(diferenca,"A.C.")
