X_stick = int(input())
stick = [64]
count = -1
while True:
    if sum(stick)>X_stick: # 더한 값이 클 경우
        stick.append(int(stick[-1]/2))
        stick[-2] = int(stick[-2]/2)
        if sum(stick)>X_stick:
            stick.pop(-2)
    elif sum(stick)<X_stick:#더한 값이 작을경우
        stick.append(int(stick[-1]/2))
        if sum(stick)>X_stick:#더한 값이 클 경우
            stick[-1] = (int(stick[-1]/2))
    if sum(stick) == X_stick:
        break
print(len(stick))