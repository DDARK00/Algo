import sys
input=sys.stdin.readline


def solve():
    n=int(input())
    lst=[tuple(map(int,input().split())) for _ in range(n)]
    power=[0,0,0]
    time=0
    ok=True
    for a, b, c, p in lst:
        if power[0]<a:
            time+=a-power[0]
            power[0]=a
        if power[1]<b:
            time+=b-power[1]
            power[1]=b
        if power[2]<c:
            time+=c-power[2]
            power[2]=c
        if time>=p:
            ok=False
            break
        else:
            time+=1
    print(ok and "YES" or "NO")
    return

def init():
    t=int(input())
    for _ in range(t):
        solve()

init()