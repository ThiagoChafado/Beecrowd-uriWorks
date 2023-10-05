linha1 = input() .split()#inicio da entrada dos primeiros dados
codigo1 = int(linha1[0])
pecas1 = int(linha1[1])
valor1 = float(linha1[2])

linha2 = input() .split()#inicio entrada segundos dados
codigo2 = int(linha2[0])
pecas2 = int(linha2[1])
valor2 = float(linha2[2])

soma1 = (pecas1 * valor1)#soma primeiros dados
soma2 = (pecas2 * valor2)#soma segundos dados
somat = (soma1 + soma2)#soma total

print(f"VALOR A PAGAR: R$ {somat:.2f}") #soma dos dois