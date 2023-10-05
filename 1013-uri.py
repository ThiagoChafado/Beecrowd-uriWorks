#entrada
linha = input() .split()
A = int(linha[0])
B = int(linha[1])
C = int(linha[2])

formulaAB = (A + B + abs(A - B))/2

if formulaAB > C:
    print(f"{formulaAB:.0f} eh o maior")
else:
    print(C, "eh o maior")
