import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

lst = [input().rstrip().split(" ") for _ in range(n)]
w = input().rstrip().split(" ")
# print(w)
find = True
for i in range(len(w)-1,-1,-1):
    ispop=False
    for j in range(n):
        if lst[j] and w[i]==lst[j][-1]:
            # print(w[i], lst[j])
            lst[j].pop()
            ispop=True
            break
    if ispop:
        continue
    find = False
    break
if find:
    for i in range(n):
        if len(lst[i])>0:
            find=False
            break

if find:
    print("Possible")
else:
    print("Impossible")