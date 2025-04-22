import math
count = int(input())
l = []
for i in range(count):
    a,b = map(int,input().split())
    if a>=b:
        l.append(math.comb(a,b))
    else:
        l.append(math.comb(b,a))
for i in range(count):
    print(l[i])