n = int(input())
f = int(input())
number = 0
subtraction = str(n)
n = n - int(subtraction[-2:])
while n % f != 0:
    n += 1
    number+=1
if number<10:
    print(f"0{number}")
else:
    print(number)