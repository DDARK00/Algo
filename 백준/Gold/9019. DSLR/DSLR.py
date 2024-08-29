import sys
from collections import deque

input = sys.stdin.readline

T = int(input())


def delta(num, command):
    if command == 0:
        return (num << 1) % 10000, 'D'
    if command == 1:
        return num - 1 if num - 1 > -1 else 9999, 'S'
    if command == 2:
        return num * 10 % 10000 + num // 1000, 'L'
    if command == 3:
        return num // 10 + num % 10 * 1000, 'R'


for _ in range(T):
    start, end = map(int, input().split())

    # D 더블 2n mod 10000
    # S -1
    # L 왼쪽회전 1234 - 2341
    # R 오른쪽회전 1234 -4123

    q = deque([(start, '')])
    # bfs
    visited = [0] * 10000

    while q:
        v, o = q.popleft()
        # 변환된 숫자, 변환 타입
        if v == end:
            print(o)
            # 내 고민은 무엇인가...
            break

        if not visited[v]:
            visited[v] = 1

            for i in range(4):
                d, c = delta(v, i)
                # 4중변환

                if not visited[d]:
                    q.append((d, o + c))
