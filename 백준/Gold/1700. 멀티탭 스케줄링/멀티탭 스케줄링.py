import sys
from math import inf
from heapq import heappop, heappush
input = sys.stdin.readline
n, k = map(int,input().split())
# 페이징 기법 n칸 k번 엔제곱 가능?
# 1~100 100 2초

lst = list(map(int,input().split()))
# 전처리
pq = []
memory = [0]*(k+1)
use = 0
change = 0
for idx, val in enumerate(lst):

    try:
        next_idx = lst.index(val,idx+1)
    except:
        next_idx = inf

    # -1 이면 가장 먼저 빠짐
    # 다른 수는 클수록 먼저 빠짐
    if use<n:
        if memory[val] == 0:
            memory[val] = 1
            use+=1
        else:
            heappop(pq)
    # 빼는 횟수만
    # 전처리 끝
    else:
        if memory[val] == 0:
            memory[val] = 1
            i, v = heappop(pq)
            memory[v] = 0
            change +=1
    heappush(pq,(-next_idx, val))
print(change)