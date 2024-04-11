import sys

input = sys.stdin.readline

r, c = map(int, input().split())

maps = [list(input().rstrip()) for _ in range(r)]

adu = []  # 생존 상태, 좌표
adu_no = 1
for i in range(r):
    for j in range(c):
        if maps[i][j] == 'R':
            adu.append((i, j))
        elif maps[i][j] == 'I':
            sx = i
            sy = j

commands = list(map(int, list(input().rstrip())))
delta = [(), (1, -1), (1, 0), (1, 1), (0, -1), (0, 0), (0, 1), (-1, -1), (-1, 0), (-1, 1)]
# 1~8

m_cnt = 0
#             mx = ax - 1 if ax > sx else ay + 1 if ax < ax else 0
#             my = ay - 1 if ay > sy else ay + 1 if ay < sy else 0
end = False
for command in commands:
    maps[sx][sy] = "."
    m_cnt += 1

    nx, ny = sx + delta[command][0], sy + delta[command][1]
    if maps[nx][ny] != "R":
        maps[nx][ny] = "I"

    else:
        print(f'kraj {m_cnt}')
        end = True
        break
    sx, sy = nx, ny

    next_adu = dict()
    for ax, ay in adu:
        mx = ax + (- 1 if ax > sx else  1 if ax < sx else 0)
        my = ay + (- 1 if ay > sy else 1 if ay < sy else 0)
        if maps[mx][my] == "I":
            end = True
            print(f'kraj {m_cnt}')

            break
        # print(- 1 if ax > sx else + 1 if ax < sx else 0)
        # print(- 1 if ay > sy else + 1 if ay < sy else 0)
        # print(mx, my, ax, ay)
        if next_adu.get((mx, my)):
            next_adu[(mx, my)] += 1
        else:
            next_adu[(mx, my)] = 1
        maps[ax][ay] = "."
    # print(next_adu)
    if end:
        break
    alive_adu = []
    for key, value in next_adu.items():
        if value == 1:
            alive_adu.append(key)
            maps[key[0]][key[1]] = "R"
    adu = alive_adu
if not end:
    for m in maps:
        print("".join(m))
