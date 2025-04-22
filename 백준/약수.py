#예전코드
#n = int(input())
#l = list(map(int,input().split()))
#while True:
#    if n>1 and l[0] * l[-1] == l[1] * l[-2]:
#        print(l[0]*l[-1])
#        break
#    elif  n>1 and l[0] * l[-1] != l[1] * l[-2]:
#        l.sort()
#        continue
#    else:
#        print(l[0]*l[-1])
#        break


#현재 코드
n = int(input())
l = list(map(int,input().split()))
l.sort()
print(l[0]*l[-1])