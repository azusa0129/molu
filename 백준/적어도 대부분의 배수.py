number = list(map(int,input().split()))
m = min(number)
while True:
    count = 0
    for i in number:
        if m % i == 0:
            count += 1
    if count >= 3:
        break
    m += 1
print(m)