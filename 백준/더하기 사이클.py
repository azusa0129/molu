l = list(input())
l.append(' ')
l.append(' ')
if len(l) < 4:
    l[1] = l[0]
    l[0] = '0'
    l.append(' ')
var = ' '
var = str(int(l[0]) + int(l[1]))
l[2] = l[1]
l[3] = var[-1]
count = 1
while True:
    if l[0:2] == l[2:4]:
        print(count)
        break
    var = str(int(l[2]) + int(l[3]))
    l[2] = l[3]
    l[3] = var[-1]
    count += 1