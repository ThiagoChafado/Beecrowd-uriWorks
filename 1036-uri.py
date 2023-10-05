import math
linha = input() .split()

A = float(linha[0])
B = float(linha[1])
C = float(linha[2])

try:
    delta = B * B -4 * A * C
    R1 = ((-B) + math.sqrt(delta))/(2 * A)
    R2 = ((-B) - math.sqrt(delta))/(2 * A)
    print(f"R1 = {R1:.5f}"),round
    print(f"R2 = {R2:.5f}"),round 

except:
    print("Impossivel calcular")
    