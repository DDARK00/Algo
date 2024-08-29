import sys

from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):

    q = deque([])

    n, o = map(int, input().split())

    # 개수, 궁금한거

    pri = []

    # idx의 우선순위

    for idx, item in enumerate(input().split()):

        q.append((idx, item))

        pri.append(item)

    pri.sort()

    cnt = 0

    # 출력 횟수

    while q:

        target = q.popleft()

        if target[1] == pri[-1]:

            if target[0] == o:

                print(cnt+1)

                break

            else:

                pri.pop()

                cnt+=1

                continue

        else:

            q.append(target)

        # 우선순위가 제일 높다면 아웃

# 시간초과는 