import sys

sys.setrecursionlimit(1000000)

input = sys.stdin.readline

n, r, q = map(int, input().split())
# 정점 수, 루트, 쿼리의 수

tree = {}

for i in range(1, n + 1):
    tree[i] = []
for _ in range(n - 1):
    # a, b를 잇는 간선,
    u, v = map(int, input().split())

    tree[u].append(v)
    tree[v].append(u)

# 정점 U를 루트로 하는 서브트리에 속한 정점의 수를 출력한다.

# 마지막 노드까지 가서, 부모가 있으면 부모에 자식 노드의 수(+본인)를 쥐여준다

# 루트 r
visited = {}

child_cnt = [0] * (n + 1)


def dfs(root):
    if not visited.get(root):
        visited[root] = 1
        child = 1
        for c in tree[root]:
            child += dfs(c)
        child_cnt[root] = child
        return child

    else:
        return 0


dfs(r)
# print(child_cnt)
for _ in range(q):
    print(child_cnt[int(input())])
# 메모를해야되구나...

# 트리+dp라길래 점화식을 트리에 박는가했는데 그냥 메모였다...
