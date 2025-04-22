n = int(input())
f = 0
l = []
for i in range(n):
    a,b = map(int,input().split())
    while b>5:
        b-=4
    f = a**b
    f = str(f)
    if f[-1] == '0':
        l.append('10')
    else:
        l.append(f[-1])
for i in range(n):
    print(l[i])