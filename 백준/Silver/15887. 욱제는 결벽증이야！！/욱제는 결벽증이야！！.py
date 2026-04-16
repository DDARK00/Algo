import sys
input=sys.stdin.readline

n=int(input())
lst=list(map(int,input().split()))
cnt=0
ans=[]
# 5 4 3 2 1
for i in range(n):
    for j in range(0,n-i-1):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
            cnt+=1
            ans.append(str(j+1)+' '+str(j+2))
print(cnt)
print(*ans,sep='\n')