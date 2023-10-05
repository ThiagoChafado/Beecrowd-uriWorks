combustivel = 0
contador1=0
contador2=0
contador3=0
while combustivel != 4 :
    combustivel=int(input())
    if combustivel == 1:
        contador1 +=1
    if combustivel ==2:
        contador2 +=1
    if combustivel ==3:
        contador3 +=1
print("MUITO OBRIGADO")
print("Alcool:",contador1)
print("Gasolina:",contador2)
print("Diesel:",contador3)
