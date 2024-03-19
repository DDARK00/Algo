import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    # 편의점 수
    hx, hy = map(int, input().split())
    # 상근이네 집

    # 맥주 한 박스에는 맥주가 20개, 한 박스 들고 출발
    # 박스에 들어있는 맥주는 20병을 넘을 수 없다.
    # 20*50 1000미터를 갈 수 있다.

    conv = [tuple(map(int,input().split())) for _ in range(n)]
    # 편의점
    tx, ty = map(int, input().split())
    # 펜타포트 좌표

    # 각 좌표는 두 정수 x와 y로 이루어져 있다. (두 값 모두 미터, -32768 ≤ x, y ≤ 32767)
    # 두 좌표 사이의 거리는 x 좌표의 차이 + y 좌표의 차이 이다. (맨해튼 거리)

    # start -> target
    # 1000 1000 -> 2000 2000 거리는 2000
    # print(conv)
    # print(tx, ty)
    # bfs
    q = deque([(hx, hy)])
    visited = {}
    # x,y에서 출발을 해서,,,
    # 전처리를 해야 하니...

    happy = False
    while q:
        x, y = q.popleft()
        # print(x, y)
        if abs(x - tx) + abs(y - ty) <= 1000:
            happy = True
            break

        for dx, dy in conv:
            if abs(dx - x) + abs(dy - y) <= 1000 and not visited.get((dx, dy)):
                visited[(dx, dy)] = 1
                q.append((dx, dy))
    # print(visited)
    if happy:
        print('happy')
    else:
        print('sad')