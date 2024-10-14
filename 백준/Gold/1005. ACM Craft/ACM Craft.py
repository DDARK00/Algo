import sys
from collections import defaultdict
input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int ,input().split())
    time = [0]+list(map(int, input().split()))
    g = defaultdict(list)
    chk = [0]*(n+1)

    for _ in range(k):
        x, y = map(int, input().split())
        chk[y]+=1
        g[x].append(y)

    w = int(input())
    st = []
    before = [0]*(n+1)

    for i in range(1, n+1):
        if chk[i] == 0:
            st.append(i)
            chk[i] = -1

        while st:
            v = st.pop()
            for num in g[v]:
                chk[num]-=1
                before[num] = max(before[num],before[v]+time[v])

                if chk[num] == 0:
                    chk[num] = -1
                    st.append(num)

    print(before[w]+time[w])