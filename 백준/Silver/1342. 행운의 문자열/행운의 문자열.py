import sys
s = sys.stdin.readline().rstrip()

n=len(s)

ans = 0

def dfs(k,bc):
    global ans
    if k == n:
        ans+=1
        return
    for i in idx:
        if i==bc:
            continue
        if used[i]>0:
            used[i]-=1
            dfs(k+1,i)
            used[i]+=1

used = [0]*26
idx = set()
for c in s:
    used[ord(c)-97]+=1
    idx.add(ord(c)-97)
idx = list(idx)

dfs(0,None)
print(ans)