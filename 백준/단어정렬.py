n = int(input())
l = []
count = 0
l1 = []
f = []
for i in range(n): #값을 넣음
    l.append(input())
l = list(set(l))
l.sort(key=lambda word:(len(word), word))
for i in range(len(l)):
    print(l[i])