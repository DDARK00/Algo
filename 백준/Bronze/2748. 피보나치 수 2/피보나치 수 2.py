n = int(input())


def fib(n):
    if n == 0 or n == 1 :
        return 1
    return fib(n-1)+fib(n-2)

fibT = [0] * (n+1)
fibT[1] = 1
for i in range(2, n+1):
    fibT[i] = fibT[i-1]+fibT[i-2]

print(fibT[n])