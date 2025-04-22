n = int(input())
f = []
for _ in range(n):
    a = [] # 손님
    b = {} # 차번호 
    O_L = 0
    h,l = map(int,input().split())

    for i in range(h): #차량 위치 
        li = list(map(int,input().split()))
        for k in range(len(li)):
            if li[k] != -1:
                a.append(li[k])
                b[li[k]] = (i+1,k+1)

    a.sort()
    value = 0
    hh = [1] * (h + 1)

    for i in range(1,len(a)+1):
        height, line = b[i]
        value += abs(1 - height)*20
        O_L = hh[height]
        clack1 = abs(O_L - line)
        clack2 = l-clack1
        value += min(clack1,clack2)*5
        hh[height] = line
    f.append(value)
print(*f)