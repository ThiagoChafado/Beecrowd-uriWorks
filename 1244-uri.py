N=int(input())
for c in range(N):
  valor = input().split()
  valor.sort(key=len, reverse=True)
  for i in range(len(valor)):
      print(valor[i], end = '')
      if i != len(valor)-1:
          print(' ', end = '')
  print()
    

