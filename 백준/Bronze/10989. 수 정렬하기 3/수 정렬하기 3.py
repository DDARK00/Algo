import sys
input = sys.stdin.readline

n = int(input())

# 10,000 보다 작거나 같은 수

arr = [0] * 10001

for _ in range(n):
    n_int = int(input())
    arr[n_int] += 1

for idx, el in enumerate(arr):
    if el != 0:
        while el > 0:
            print(idx)
            el -= 1
