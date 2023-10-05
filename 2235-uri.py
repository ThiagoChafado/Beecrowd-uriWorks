linha1 = input() .split()
A = int(linha1[0])
B = int(linha1[1])
C = int(linha1[2])

#2 viagens
if ((A - B ==0) or (A - C == 0) or (B - C == 0)):
    print("S")
    #3 viagens
else:
    if ((A + B - C == 0) or (A + C - B ==0) or (B + C -A ==0)):
        print("S")
    elif((A - B- C == 0) or (B - A - C == 0) or (C - A - B == 0)):
        print("S")
    else:
        print("N")