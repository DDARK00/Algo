from collections import deque

n = int(input())

deq = deque()
lst = list(map(int, input().split()))
lst.sort()
deq.extend(lst)
# 덱 세팅

max_m = 0
if len(deq) % 2 == 0:
# 원소가 짝수개면?
    while deq:
        l = deq.popleft()
        r = deq.pop()
        max_m = max(l+r,max_m)
else:
    # 홀수개면
    max_m = deq.pop()
    while deq:
        l = deq.popleft()
        r = deq.pop()
        max_m = max(l+r,max_m)

print(max_m)