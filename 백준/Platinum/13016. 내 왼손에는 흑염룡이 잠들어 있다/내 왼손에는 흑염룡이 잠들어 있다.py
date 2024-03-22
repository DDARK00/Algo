import sys

input = sys.stdin.readline
n = int(input())
g = [[] for _ in range(n + 1)]

# 각 도로는 두 국가를 양방향으로 연결한다.
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    g[a].append((c, b))
    g[b].append((c, a))


def dfs(idx):
    st = [(0, idx)]  # 거리와 v
    visited = [0] * (n + 1)

    distance = [-1] * (n + 1)
    distance[idx] = 0
    while st:
        w, v = st.pop()

        for nw, nv in g[v]:
            if distance[nv] == -1:
                distance[nv] = nw + w
                st.append((nw + w, nv))
    # print(distance)
    # print(max(distance))
    max_idx = -1
    max_val = -1
    for idxx, dist in enumerate(distance):
        if dist > max_val:
            max_val = dist
            max_idx = idxx

    return max_idx, distance


# print(g)

idx = dfs(1)[0]
idx2, dist2 = dfs(idx)
idx3, dist3 = dfs(idx2)
for i in range(1, n + 1):
    print(max(dist2[i], dist3[i]))
