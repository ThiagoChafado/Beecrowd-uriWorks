N = int(input())
for i in range(N):
  lista = sorted(list(map(str, input().split(' '))))
  listacerta = list()
  for j in lista:
    if j not in listacerta:
      listacerta.append(j)
  print(' '.join(listacerta))  