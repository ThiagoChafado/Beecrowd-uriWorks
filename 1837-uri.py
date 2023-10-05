line = input() .split()
a = int(line[0])
b = int(line[1])
q = a // b
r = a % b
while r <0 :
    r = r + (abs (b))
    q = q + 1

print(q,r)