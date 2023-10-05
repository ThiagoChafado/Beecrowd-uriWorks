N = int(input())
a= 0
b = 1
for contador in range(0,N,):
    if contador ==N-1:
        print(a)
    else:
        print(a,end=' ')
    soma = a+b
    a = b
    b = soma
    
    

