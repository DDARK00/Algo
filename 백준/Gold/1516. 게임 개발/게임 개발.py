import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())

deg = [0]*(n+1)
before = defaultdict(list)
time = [0]*(n+1)

for i in range(1, 1+n):
    l = list(map(int, input().split()))
    j = 1
    while True:
        if l[j] == -1:
            break
        deg[i]+=1
        before[l[j]].append(i)
        j+=1
    time[i] = l[0]

ans = [0]*(n+1)
st = []
for i in range(1, 1+n):
    if deg[i] == 0:
        deg[i] = -1
        st.append(i)

    while st:
        v = st.pop()
        ans[v]+=time[v]
        for num in before[v]:
            deg[num]-=1
            ans[num] = max(ans[v], ans[num])
            if deg[num] == 0:
                st.append(num)
                deg[num] = -1
for i in range(1, 1+n):
    print(ans[i])