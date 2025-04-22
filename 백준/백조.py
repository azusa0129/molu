l = []
a,b = map(int,input().split())
for i in range(a):
    l.append([])
    n = input()
    for k in range(b):
        l[i] += n[k]