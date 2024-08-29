n, m = map(int, input().split())

ar = []


def dfs(i):
    if len(ar) == m:
        print(" ".join(ar))
        # print('ok')

    for k in range(i, n + 1):
        ar.append(str(k))
        dfs(k + 1)
        ar.pop()


dfs(1)
# 하...