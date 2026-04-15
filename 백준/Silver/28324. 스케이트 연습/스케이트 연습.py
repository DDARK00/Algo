import sys
input=sys.stdin.readline

n=int(input())
answer=0
lst=list(map(int,input().split()))
bf=0
for i in range(n-1,-1,-1):
    bf=min(bf+1,lst[i])
    answer+=bf
print(answer)