import sys

input = sys.stdin.readline

# 천만에 10초

n = int(input())

lst = [101]*7

for _ in range(n):

    k = float(input())

    if lst[6]>k:

        lst.pop()

        lst.append(k)

        lst.sort()

for i in lst:

    print(f'{i:.3f}')