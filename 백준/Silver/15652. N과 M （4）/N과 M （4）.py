n, m = map(int, input().split())

ar = []


def dfs(i):
    if len(ar) == m:
        print(" ".join(ar))
        return

    for k in range(i, n + 1):
        ar.append(str(k))

        dfs(k)

        ar.pop()


dfs(1)
'''
1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
'''
