listapar=[]
listaimpar=[]
N = int(input())
for i in range(N):
  X = int(input())
  if X % 2 ==0:
    listapar.append(X)
  else:
    listaimpar.append(X)
listapar.sort()
listaimpar.sort(reverse=True)
for j in range(len(listapar)):
  print(listapar[j])
for c in range(len(listaimpar)):
  print(listaimpar[c])
