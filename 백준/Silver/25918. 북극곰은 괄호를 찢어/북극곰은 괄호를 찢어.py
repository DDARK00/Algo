import sys
input = sys.stdin.readline

n = int(input())
s = input().rstrip()

st = []
# 스택의 깊이
depth = 0
m_depth = 0
for c in s:
    if st and st[0] == c:
        depth += 1
        st.append(c)
    elif st and st[0] != c:
        depth -= 1
        st.pop()
    else:
        depth +=1
        st.append(c)
    m_depth = max(depth,m_depth)
if st:
    print(-1)
else:
    print(m_depth)