linha1 = input() .split()
n1 = float(linha1[0])
n2 = float(linha1[1])
n3 = float(linha1[2])
n4 = float(linha1[3])


media1 = n1 *2 
media2 = n2 *3
media3 = n3 *4
media4 = n4 *1
mediatotal = (media1 + media2 + media3 + media4)/10
print(f"Media: {mediatotal:.1f}")

if mediatotal >= 7:
    print("Aluno aprovado.")
elif mediatotal < 5:
    print("Aluno reprovado.")
elif mediatotal >=5 and mediatotal <7:
    print("Aluno em exame.")
    exame = float(input())
    print(f"Nota do exame: {exame:.1f}")
    mediafinal = (exame + mediatotal)/2
    mediafinal2 = (mediafinal + exame)/2
    if mediafinal >= 5:
        print("Aluno aprovado.")
        print(f"Media final: {mediafinal:.1f}")
    else:
        print("Aluno reprovado.")