import sys

input = sys.stdin.readline

n = int(input())  # 노드의 수

edges = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    edges[a].append((c, b))  # a에서 b로 가는 비용이 c
    edges[b].append((c, a))


def dfs(idx):
    visited = [10001] * (n + 1)
    st = [(0, idx)]

    visited[idx] = 0
    m_idx = -1
    m_val = 0
    while st:
        c, v = st.pop()  # 거리, 노드

        for nc, nv in edges[v]:
            if visited[nv] > c + nc:
                visited[nv] = nc + c
                if m_val < nc + c:
                    m_val = nc + c
                    m_idx = nv
                st.append((nc + c, nv))

    # print(visited)
    # print(m_idx, m_val)
    return m_idx, m_val


# 루트 노드의 번호는 항상 1
idx, val = dfs(1)
idx1, val1 = dfs(idx)
# idx2, val2 = dfs(idx1)
print(val1)
# 1. 0으로 빈 값이 최대일 수 있나?
# 답이 없으면 없는 것
