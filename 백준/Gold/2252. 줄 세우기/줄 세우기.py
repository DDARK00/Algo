import sys
from collections import defaultdict
input=sys.stdin.readline

n, m = map(int, input().split())

chk = [0]*(n+1)
wait = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    # a -> b
    chk[b]+=1
    wait[a].append(b)

st = []
for i in range(1, n+1):
    if chk[i] == 0:
        chk[i] = -1
        st.append(i)

    while st:
        v = st.pop()
        print(v, end=" ")
        for num in wait[v]:
            chk[num]-=1
            if chk[num] == 0:
                chk[num] = -1
                st.append(num)