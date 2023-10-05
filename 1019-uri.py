num = int(input())

horas = num // 3600
num -= horas * 3600

minutos = num // 60
num -= minutos * 60

segundos = num

print(f"{horas}:{minutos}:{segundos}")
