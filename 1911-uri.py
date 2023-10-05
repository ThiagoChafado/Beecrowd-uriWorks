while True:
    numero_alunos = int(input())
    if numero_alunos == 0:
        break
    dicionario={}
    for i in range(numero_alunos):
      nomes = input().split(' ')
      dicionario[nomes[0]]=nomes[1]
    quevieram = int(input())
    a = 0
    b = 0
    for x in range(quevieram):
      contagem=0
      confirmacao=input().split(' ')
      for y in dicionario[confirmacao[0]]:
        if y != confirmacao[1][contagem]:
          a+=1
        contagem+=1
      if a >1:
        b+=1
      a=0
    print(b)