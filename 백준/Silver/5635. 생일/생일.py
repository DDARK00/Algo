T = int(input())

lst = [[0] for _ in range(T)]
for t in range(T):
    n, d, m, y = input().split()
    lst[t] = [n, int(d), int(m), int(y)]
lst.sort(key=lambda x: (x[3], x[2], x[1]) or None)
print(lst[T-1][0])
print(lst[0][0])
