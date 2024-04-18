import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
# 기술 3가지
# 1. 맨 위 하나 바닥에 놓기
# 2. 위에서 2장째 바닥에 놓기
# 3. 제일 밑장 바닥에 놓기
cards = [i for i in range(n, 0,-1)]
# 이 상태였다 거꾸로 뒤집으면 되나

skills = list(map(int, input().split()))
origin = deque([])
# 출력은 위에서 아래로
# 카드뭉치는 위에서 아래로 1~~ N
for i in range(n - 1, -1, -1):
    skill = skills[i]
    card = cards.pop()
    if skill == 1:  # 왼쪽이 위 오른쪽이 아래(원래 카드뭉치)
        origin.appendleft(card)
    elif skill == 2:
        temp = origin.popleft()
        origin.appendleft(card)
        origin.appendleft(temp)
    elif skill == 3:
        origin.append(card)
print(*origin)
