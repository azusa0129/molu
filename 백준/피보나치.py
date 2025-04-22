dp = [0] * 41
def fibonacci(n):
    if dp[n]: return dp[n]
    if n == 0:
        dp[n] = [1, 0]
        return [1,0]
    elif n == 1:
        dp[n] = [0, 1]
        return [0,1]
    else:
        d = fibonacci(n-1)
        g = fibonacci(n-2)
        dp[n] = [d[0]+g[0], d[1]+g[1]] 
        return [d[0]+g[0], d[1]+g[1]]
a = int(input())
l = []
for i in range(a):
    b = int(input())
    l.append(fibonacci(b))
for result in l:
    print(result[0], result[1])
