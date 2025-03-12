import sys
input=sys.stdin.readline

st = []
d = {}
d[1] = lambda x: st.append(x[0])
d[2] = lambda x: print(st.pop() if st else -1)
d[3] = lambda x: print(len(st))
d[4] = lambda x: print(0 if st else 1)
d[5] = lambda x: print(st[-1] if st else -1)
for _ in range(int(input())):
    c, *x = map(int, input().split())
    d[c](x)