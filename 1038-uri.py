linha1 = input() .split()
codigo = int(linha1[0])
quant = int(linha1[1])
dogao = 4
xsalada = 4.50
xbacon = 5
torrada = 2
refri = 1.50


if codigo  == 1:
    print(f"Total: R$ {dogao * quant:.2f}")
elif codigo == 2:
    print(f"Total: R$ {xsalada * quant:.2f}")
elif codigo == 3:
    print(f"Total: R$ {xbacon * quant:.2f}")
elif codigo == 4:
    print(f"Total: R$ {torrada * quant:.2f}")
elif codigo == 5:
    print(f"Total: R$ {refri * quant:.2f}")
