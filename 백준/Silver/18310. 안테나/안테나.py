import sys

input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))

lst.sort()
mid = n // 2 if n % 2 == 0 else n // 2 + 1  # 6->  3-1  / 7 -> 3 + 1 - 1
print(lst[mid-1])
