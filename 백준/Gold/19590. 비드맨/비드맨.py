import sys
input=sys.stdin.readline
# 3 3 3 -> 1 9%2
# 1 1 3 -> 1 5%2
# 2 2 3 -> 1 7%2

# 3333 0 12%2
# 2333 1 11%2
biz = [int(input()) for _ in range(int(input()))]

m_v = 0
s = 0
for item in biz:
    s +=item
    m_v = item if m_v < item else m_v

etc = s-m_v
if etc<m_v: # 
    print(m_v-etc)
else:
    print(s%2 or 0)