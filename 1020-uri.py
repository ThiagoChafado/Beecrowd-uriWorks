num = int(input())
ano = num // 365
num -= ano * 365

mes = num // 30
num -=mes * 30

dia = num


print(ano,"ano(s)")
print(mes,"mes(es)")