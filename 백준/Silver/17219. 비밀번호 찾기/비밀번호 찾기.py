import sys

input = sys.stdin.readline

n, m = map(int, input().split())

memo = {}
for _ in range(n):
    a, b = input().split()
    memo[a] = b

for _ in range(m):
    q = input().strip()
    print(memo[q])
