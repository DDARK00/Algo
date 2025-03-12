import sys
input=sys.stdin.readline

n=int(input())
sc = [0, 0]
t = 0
ans = [0, 0]


def calc(td):
    if sc[0]>sc[1]:
        ans[0] += td-t
    else:
        ans[1] += td-t

for _ in range(n):
    i, to = input().split()
    i = int(i)-1
    m, s = map(int, to.split(":"))
    td = m*60 + s
    if sc[0] != sc[1]:
        calc(td)
    t = td
    sc[i]+=1
if sc[0]!=sc[1]:
    calc(48*60)
print(*map(lambda x:f"00{x//60}"[-2:]+":"+f"00{x%60}"[-2:],ans),sep='\n')