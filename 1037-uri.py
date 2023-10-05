num = float(input())
intervalo1 = "Intervalo [0,25]"
intervalo2 = "Intervalo (25,50]"
intervalo3 = "Intervalo (50,75]"
intervalo4 = "Intervalo (75,100]"




if num >= 0 and num <=25 :
    print(intervalo1)
elif num > 25 and num <=50:
    print(intervalo2)
elif num >50 and num <=75:
    print(intervalo3)
elif num >75 and num <=100:
    print(intervalo4)
else:
    print("Fora de intervalo")
