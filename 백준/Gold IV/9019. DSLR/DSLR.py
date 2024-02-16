import sys
from collections import deque

input = sys.stdin.readline

T = int(input())


def delta(num, command):
    if command == 0:
        return num * 2 % 10000, 'D'
    if command == 1:
        return num - 1 if num - 1 > -1 else 9999, 'S'
    if command == 2:
        return num * 10 % 10000 + num // 1000, 'L'
    if command == 3:
        return num // 10 + num % 10 * 1000, 'R'


for _ in range(T):
    start, end = input().split()

    # D 더블 2n mod 10000
    # S -1
    # L 왼쪽회전 1234 - 2341
    # R 오른쪽회전 1234 -4123

    q = deque([(int(start), '')])
    # bfs
    visited = [0] * 10000

    while q:
        v, o = q.popleft()
        # 변환된 숫자, 변환 타입
        if v == int(end):
            print(o)
            # 와 이런 방법이 있었구나 하.........걍 부모 노드 정보를 자식 노드에 넘겨주고 계속 이어가면 되는 것이었따....
            # 내 고민은 무엇인가...
            break

        if not visited[v]:
            visited[v] = 1

            for i in range(4):
                d, c = delta(v, i)
                # 4중변환

                if not visited[d]:
                    q.append((d, o+c))
                    # 부모 노드 기억...? 어떻게 깔끔하게 하지
