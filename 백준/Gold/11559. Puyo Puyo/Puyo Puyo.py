import sys
from collections import deque

input = sys.stdin.readline

# 총 12개의 줄에 필드의 정보가 주어지며, 각 줄에는 6개의 문자가 있다.

# R은 빨강, G는 초록, B는 파랑, P는 보라, Y는 노랑이다.

lst = [input().rstrip() for _ in range(12)]

lst = list(map(list, zip(*lst[::-1])))
# 배열 가로로 돌려서 bfs 후 .으로 바꾸고 . 을 날리기 + 재구축
# 시간 충분하겠죠?

def find_puyo():
    select = []
    visited = [[0] * 12 for _ in range(6)]
    for i in range(6):
        for j in range(12):
            if not visited[i][j]:
                visited[i][j] = 1

            if lst[i][j] != ".":
                target = lst[i][j]
                q = deque([(i, j)])
                waiting = [(i, j)]
                while q:
                    x, y = q.popleft()

                    for dx, dy in [(0, 1), (1, 0), (-1, 0,), (0, -1)]:
                        if 0 <= x + dx < 6 and 0 <= y + dy < 12 and not visited[x + dx][y + dy] and \
                                lst[x + dx][y + dy] == target:
                            visited[x + dx][y + dy] = 1
                            waiting.append((x + dx, y + dy))
                            q.append((x + dx, y + dy))
                if len(waiting) >= 4:
                    select.extend(waiting)
    return select  # 지울 뿌요 목록


def remove_puyo(puyo_lst: list):
    if not puyo_lst:
        return
    global ren
    global lst

    ren += 1
    for px, py in puyo_lst:
        lst[px][py] = "."


def move_puyo(punk_lst: list):
    n_lst = []
    for ls in punk_lst:
        puyos = "".join(ls).replace(".", "")
        n_lst.append(list(puyos + "." * (12 - len(puyos))))
    return n_lst


ren = 0

while True:
    del_lst = find_puyo()
    if not del_lst:
        break
    remove_puyo(del_lst)
    lst = move_puyo(lst)

print(ren)
