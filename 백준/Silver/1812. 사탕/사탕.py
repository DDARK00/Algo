import sys
input=sys.stdin.readline
n=int(input())
cnt=[int(input()) for _ in range(n)]

for i in range(cnt[0]+1):
    answer=[]
    ok=0
    answer.append(i)
    for j in range(n-1):
        k=cnt[j]-answer[-1]
        if k<0:
            break
        else:
            answer.append(k)
            ok+=1
    if ok==n-1 and answer[0]+answer[-1] == cnt[-1]:
        print(*answer, sep='\n')
        break