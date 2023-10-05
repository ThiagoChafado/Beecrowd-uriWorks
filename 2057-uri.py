linha1 = input() .split()
S = int(linha1[0])
T = int(linha1[1])
F = int(linha1[2])
chegada = S + T + F

if chegada >=0 and chegada <24:
    print(chegada)
elif chegada > 24:
    chegada = chegada % 24
    print(chegada)
elif chegada <=0:
    chegada = chegada + 24
    print(chegada)
elif chegada == 24:
    chegada = 0
    print(chegada)