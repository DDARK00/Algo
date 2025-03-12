a,b,c=map(int,input().split())
#ax+by=c
ans = [[] for _ in range(11)]
for i in range(1,11):
    for j in range(1,11):
        if i*a+j*b == c:
            ans[i].append(j)
ans=ans[1:]
for lst in ans:
    if lst:
        print(*lst)
    else:
        print(0)