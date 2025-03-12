import sys
from collections import defaultdict as d
input=sys.stdin.readline

n, m = map(int, input().split())

g = d(lambda: {"day":0, "time":0})
dns = set()
for _ in range(n):
    # 입력 순서는 방송 날짜의 오름차순이 아닐 수 있다.
    name, day, st, ed = input().split()
    week = (int(day)-1)//7
    sh, sm = map(int, st.split(":"))
    eh, em = map(int, ed.split(":"))
    time = eh*60+em-sh*60-sm
    g[name+str(week)]["day"]+=1
    g[name+str(week)]["time"]+=time
    dns.add(name)
ans = []
for name in list(dns):
    honmono = True
    for i in range(m//7):
        if g[name+str(i)]["day"]>=5 and g[name+(str(i))]["time"]>=3600:
            continue
        else:
            honmono = False
            break
    if honmono:
        ans.append(name)

if ans:
    print(*sorted(ans), sep="\n")
else:
    print(-1)
    