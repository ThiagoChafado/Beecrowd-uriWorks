linha1 = input() .split()
A = float(linha1[0])
B = float(linha1[1])
C = float(linha1[2])
primeiro = float(1)
segundo = float(1)
terceiro = float(1)

#ordenar
if A >= B and A >= C:
    primeiro = A
    if B >= C:
        segundo = B
        terceiro = C
    else:
        segundo = C
        terceiro = B
if B >= A and B >= C:
    primeiro = B
    if A >= C:
        segundo = A
        terceiro = C
    else:
        segundo = C
        terceiro = A
if C >= A and C >= B:
    primeiro = C
    if B >= A:
        segundo = B
        terceiro = A
    else:
        segundo = A
        terceiro = B

#classificar

if  primeiro >= (segundo + terceiro):
    print("NAO FORMA TRIANGULO")
else:
    if (primeiro**2) == (segundo**2) + (terceiro**2):
        print("TRIANGULO RETANGULO")
    elif (primeiro**2) > (segundo**2) + (terceiro**2):
        print("TRIANGULO OBTUSANGULO")
    elif (primeiro**2) < (segundo**2) + (terceiro**2):
        print("TRIANGULO ACUTANGULO")
if (primeiro == segundo and segundo == terceiro):
     print("TRIANGULO EQUILATERO")
elif primeiro == segundo != terceiro or segundo == terceiro != primeiro or primeiro == terceiro != segundo:
    print("TRIANGULO ISOSCELES")