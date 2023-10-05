linha = input() .split() #entrada
A = float(linha[0])
B = float(linha[1])
C = float(linha[2])

#triangulo
triangulo = (A * C)/2 
print(f"TRIANGULO: {triangulo:.3f}")

#circulo
pi = 3.14159
circulo = C * C * pi
print(f"CIRCULO: {circulo:.3f}")

#trapézio
trapezio = (A + B) * C/2
print(f"TRAPEZIO: {trapezio:.3f}")

#quadrado
quadrado = B * B
print(f"QUADRADO: {quadrado:.3f}")

#retangulo
retangulo = A * B
print(f"RETANGULO: {retangulo:.3f}")
