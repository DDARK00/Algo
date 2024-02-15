import sys
from collections import deque

input = sys.stdin.readline

deq = []

n = int(input())

for _ in range(n):
    deq.append(deque(input().rstrip()))

    # 톱니바퀴 세팅, 12시방향부터 8개 N극은0 S극은1
    # 닿는 부분 -> 3이랑 7

k = int(input())
# 회전 횟수
for _ in range(k):
    # k번 회전,
    unit, direction = map(int, input().split())
    # unit번을 1은 시계방향 -1은 반시계방향
    # 시계방향 -> 오른쪽으로 한 칸 밀기
    # 반시계는 반대로
    # unit index 1만큼 차이

    target_left = deq[unit - 1][6]
    target_right = deq[unit - 1][2]
    # 타겟 - 현재 돌리는 톱니바퀴 - 같으면 돌고 아니면 말고

    # 왼쪽 돌리고 오른쪽 돌리고
    # unit-1이 현재 인덱스
    temp_left = target_left
    left_turn = direction
    for i in range(unit - 2, -1, -1):
        # 현재의 왼쪽거부터 파도타기
        # 돌릴 경우를 대비해서 현재 왼쪽 축의 극 저장
        if deq[i][2] != temp_left:
            temp_left = deq[i][6]
            # 같지 않으면 돌리기
            if left_turn == -1:
                deq[i].rotate(1)
                left_turn = 1
            else:
                deq[i].rotate(-1)
                left_turn = -1
        else:
            break
            # 같으면 그만 돌리기

    temp_right = target_right
    right_turn = direction
    # 현재의 우측 톱니
    for i in range(unit, n):
        if deq[i][6] != temp_right:
            temp_right = deq[i][2]

            if right_turn == -1:
                deq[i].rotate(1)
                right_turn = 1
            else:
                deq[i].rotate(-1)
                right_turn = -1
        else:
            break

    # 옆에 다 돌리고 자기도 돌기
    deq[unit-1].rotate(direction)
cnt = 0
for deqq in deq:
    cnt += 1 if deqq[0][0] =='1' else 0
print(cnt)