def fibonacci(n):
    if  n == 1 or n == 2:
        return 1

    f = [0] * (n + 1)
    f[1] = f[2] = 1

    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]

    return f[n]
n = int(input())

print(fibonacci(n), n-2)