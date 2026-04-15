import sys
input=sys.stdin.readline

n=int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]
# n=8
answer=0
def dfs(now):
    global answer
    if now==n:
        ans=0
        for hp, atk in eggs:
            if hp<=0:
                ans+=1
        answer=max(ans,answer)
        return

    if eggs[now][0]<=0:
        dfs(now+1)
        return

    # hp, 공격력
    # now으로 target을 친다
    crash=False
    for target in range(n):
        if target==now:
            continue

        if eggs[target][0] > 0:
            eggs[now][0]-=eggs[target][1]
            eggs[target][0]-=eggs[now][1]
            dfs(now+1)
            eggs[now][0]+=eggs[target][1]
            eggs[target][0]+=eggs[now][1]
            crash=True
        else:
            dfs(now+1)

    if not crash:
        dfs(n)

def solve():
    dfs(0)
    print(answer)

solve()