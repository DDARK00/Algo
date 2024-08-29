import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [input().rstrip() for _ in range(n)]

dna = {"A":0,"C":1,"G":2,"T":3}

ans = [[0]*4 for _ in range(m)]

for i in range(n):
    for j in range(m):
        c = lst[i][j]
        idx = dna[c]
        ans[j][idx]+=1
fdx = ["A","C","G","T"]
cnt = 0
for a,c,g,t in ans:
    m_val = max(a,c,g,t)
    idx = [a,c,g,t].index(m_val)
    cnt += n-m_val
    print(fdx[idx], end="")
print("")
print(cnt)