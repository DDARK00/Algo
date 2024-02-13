n, m = map(int, input().split())

ar = []


def dfs(i):
    if len(ar) == m:
        print(" ".join(ar))
        return

    for k in range(i, n + 1):
        if str(k) not in ar:
            ar.append(str(k))
            dfs(i)
            ar.pop()


dfs(1)
# 어휴 너무 어렵다