import sys, math
input=sys.stdin.readline

a,b,c=map(int,input().split())
s,v=map(int,input().split())
l=int(input())
left = (250-l)*100
answer=0
for e, cnt in sorted([(a,-1),(b,s*30),(c,v*30)],key=lambda x:-x[0]):
    if cnt==0:
        continue
    if cnt==-1 or e*cnt>left:
        answer+=math.ceil(left/e)
        break
    left-=e*cnt
    answer+=cnt
print(answer)