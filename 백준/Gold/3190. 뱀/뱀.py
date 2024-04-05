from collections import deque
import sys

input = sys.stdin.readline

n = int(input())  # 보드의 크기

k = int(input())  # 사과의 개수

q = deque([(0, 0)])  # 맨위 맨좌측

lst = [[0] * n for _ in range(n)]

d = 0
# 0이 동쪽이라고 하자 j+1
# 1이 남쪽 i+1
# 2 서 j-1
# 3 북 i-1
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for _ in range(k):
    a, b = map(int, input().split())
    lst[a - 1][b - 1] = 2
# 사과의 위치

l = int(input())  # 방향 변환 횟수
move_cnt = 0
lst[0][0] = 1
command = [''] * 10001  # 100*100
# print(command)

for _ in range(l):
    x, c = input().split()
    command[int(x)] = c

while q:
    move_cnt += 1
    # 머리가 deque의 -1에 위치?
    # 꼬리가 0
    head = q[-1]
    nx = head[0] + delta[d][0]
    ny = head[1] + delta[d][1]
    # 다음 머리가 갈 곳
    # print(nx,ny)
    if 0 <= nx < n and 0 <= ny < n and lst[nx][ny] != 1:
        q.append((nx, ny))
        if lst[nx][ny] != 2:
            bx, by = q.popleft()
            lst[bx][by] = 0
        lst[nx][ny] = 1
    else:
        break
    # 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도

    if command[move_cnt]:  # 왼쪽 -1   오른쪽 +1
        d = (d + 5) % 4 if command[move_cnt] == 'D' else (d + 3) % 4

print(move_cnt)
