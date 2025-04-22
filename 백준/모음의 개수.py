l = []
count = 0
while True:
    l.append(input())
    if '#' in l:
        break
for i in range(len(l)-1):
    for k in range(len(l[i])):
        if 'a' == l[i][k] or 'e' == l[i][k] or 'i' == l[i][k] or 'o' == l[i][k] or 'u' == l[i][k] or 'A' == l[i][k] or 'E' == l[i][k] or 'I' == l[i][k] or 'O' == l[i][k] or 'U' == l[i][k]:
            count += 1
    print(count)
    count = 0