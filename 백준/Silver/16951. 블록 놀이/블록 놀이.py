import sys
input=sys.stdin.readline

n,k=map(int,input().split())
lst=list(map(int,input().split()))

answer=1e9

for i in range(1,max(lst)+1):
    tmp=i
    tmp_ans=int(lst[0]!=i)
    for j in range(1,n):
        if lst[j]-tmp != k:
            tmp_ans+=1
        tmp+=k
        if tmp_ans>answer:
            break
    answer=min(answer,tmp_ans)
print(answer)