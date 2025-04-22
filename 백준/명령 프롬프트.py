n = int(input())
l = [input() for _ in range(n)]
f = [''] * len(l[0])
for i in range(len(l[0])):
    if n == 1:
        print(l[0])
        break
    for k in range(1,n):
        if l[k][i] != l[0][i]:
            f[i] = '?'
            break
        else:
            f[i] = l[0][i]
for i in range(len(f)):
    print(f[i],end = "")
print()