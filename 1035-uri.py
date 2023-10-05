linha1 = input() .split()
A = int(linha1[0])
B = int(linha1[1])
C = int(linha1[2])
D = int(linha1[3])

CD = C + D
AB = A + B

if (B > C and D > A and CD > AB and C >= 0 and D >= 0 and A//2):
    print("Valores aceitos")
else: 
    print("Valores nao aceitos")    