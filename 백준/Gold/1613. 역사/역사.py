import sys
input=sys.stdin.readline
n, k = map(int, input().split())

deg = [0]*(n+1)
lst = [[] for _ in range(n+1)]
for _ in range(k):
    a, b = map(int, input().split())
    lst[a].append(b)
    deg[b]+=1

chk = [set() for _ in range(n+1)]
st = []
for i in range(1, n+1):
    if deg[i]==0:
        st.append(i)
        chk[i].add(i)

while st:
    v = st.pop()
    for nv in lst[v]:
        deg[nv]-=1
        chk[nv] |= chk[v] # before
        chk[nv].add(v)
        if deg[nv]==0:
            st.append(nv)

for _ in range(int(input())):
    a, b = map(int, input().split())
    if b in chk[a]:
        print(1)
    elif a in chk[b]:
        print(-1)
    else:
        print(0)