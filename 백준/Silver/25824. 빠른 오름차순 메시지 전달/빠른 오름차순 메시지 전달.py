import sys
input=sys.stdin.readline

g = [list(map(int,input().split())) for _ in range(12)]

ans = 1e9
def dfs(now, dist):
    global ans

    step = now//2
    near_cost = g[step*2][step*2+1]
    if dist+near_cost>ans:
        return

    if step == 5:
        ans = dist+near_cost
        return
    # 0 -> 1 -> 2, 3
    # 1 -> 0 -> 2, 3
    for i in range(2):
        # nxt
        dfs(step*2+2+i, dist+g[now+1 if step*2==now else now-1 ][step*2+2+i]+near_cost)


def solve():
    dfs(0, 0)
    dfs(1, 0)

solve()
print(ans)