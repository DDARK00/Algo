import sys

input = sys.stdin.readline

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    maps = [input().split() for _ in range(h)]

    # dfs
    stack = []

    land = 0
    for hi in range(h):
        for wj in range(w):
            if maps[hi][wj] == "1":
                land += 1
                maps[hi][wj] = "0"
                stack.append((hi, wj))
                # print(hi, wj)
                while stack:
                    i, j = stack.pop()
                    for dx, dy in [(-1, -1,), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                        if 0 <= i + dx < h and 0 <= j + dy < w:
                            if maps[i + dx][j + dy] == "1":
                                maps[i + dx][j + dy] = "0"
                                stack.append((i + dx, j + dy))
                        # 땅을 만나면
    # print(maps)

    print(land)
