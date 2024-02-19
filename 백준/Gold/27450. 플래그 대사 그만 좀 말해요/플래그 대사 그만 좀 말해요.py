import sys

from math import ceil

from collections import deque

input = sys.stdin.readline

n, k = map(int,input().split())

#부하의 수, 목소리 크기

# 최악은 50만*2 * 50만????

now = list(map(int,input().split()))

# 목표 강화량

want = list(map(int,input().split()))

# 손실 없이 모든 파워를 받을 수 있는 위치 : 좌측

# >>>그리디

# 그래서 이걸 어떻게 저장하냐

answer = 0

# 소리친 횟수

# 좌측부터 부하, 외침 진행 fifo 큐

# k5 4 3 2 1 0

# i0 1 2 3 4 5-i  만료는5

# 0  5 4 3 2 1

# [(5:idx,3:k)]

# if q[0][0]+k >i pop

q = deque([])

added = 0

# 더해지는 파워

lost = 0

# 매 턴 감소하는 양

for i in range(n):

    if q:

        added -=lost

        if q[0][0]+k == i:

            # idx가 현재 인덱스와 같다면

            lost-=q[0][1]

            q.popleft()

    if want[i]>now[i]+added:

        p = ceil((want[i] - now[i]-added)/k) # 횟수

        answer+=p

        q.append((i,p))

        added+= p*k

        lost+=p

        # 1칸마다 1씩 감소함->횟수번 감소

        # print(q,added,lost)

print(answer)