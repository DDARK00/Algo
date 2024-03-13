import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
# n 은 자료구조의 수


a1 = input().split()
a2 = deque(input().split())

k = int(input())
# print(k)
# for target in input().split():
#
#     for i in range(n):
#         if a1[i] == "0":
#             # 큐
#             a2[i], target = target, a2[i]
#     print(target, end=" ")

lst = []
for i in range(n):
    if a1[i] == '0':
        lst.append(a2[i])
lst = deque(lst)
for target in input().split():
    lst.appendleft(target)
    print(lst.pop(), end=" ")
