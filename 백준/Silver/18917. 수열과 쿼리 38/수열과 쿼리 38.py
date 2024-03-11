import sys
from collections import deque

input = sys.stdin.readline

# 1 추가
# 2 제거  항상 A에 x가 있는 쿼리만 주어진다.
# 3 sum
# 4 xor ^
n = int(input())
sam = 0
sa = 0

for _ in range(n):
    a = input()
    if a.startswith("1"):
        num = int(a.split()[1])
        sam += num
        sa ^= num
    elif a.startswith("2"):
        num = int(a.split()[1])
        sam -= num
        sa ^= num
    elif a.startswith("3"):
        print(sam)
    else:
        print(sa)
