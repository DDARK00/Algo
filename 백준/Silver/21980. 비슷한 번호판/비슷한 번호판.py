import sys
from collections import defaultdict
input=sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    # n개 k글자수

    a = input().split()
    g = defaultdict(int)
    ans=0
    for s in a:
        cnt=0
        for c in s:
            if c.isupper():
                cnt+=1
        temp = list(s.lower())
        temp.sort()
        temp=str(cnt)+"".join(temp)
        ans+=g[temp]
        g[temp]+=1
    
    print(ans)