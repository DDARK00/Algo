import sys
input = sys.stdin.readline

n = int(input())
st = []
ans = 0
for _ in range(n):
    m = int(input())
    if st and st[-1]>m:
        ans+=len(st)
        st.append(m)
    else:
        while st and st[-1]<=m:
            st.pop()
        ans+=len(st)
        st.append(m)
print(ans)