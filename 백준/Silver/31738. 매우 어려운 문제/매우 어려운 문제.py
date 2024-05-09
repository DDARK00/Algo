n, m = map(int, input().split())

if n >= m:
    print(0)
else:
    mod = 1
    for i in range(2, n + 1):
        mod = (mod * i) % m
    print(mod)
