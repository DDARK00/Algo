import sys
input=sys.stdin.readline

lst=[]
for _ in range(int(input())):
    a,b=map(int,input().split())
    a=a//100*60+a%100-10
    b=b//100*60+b%100+10
    lst.append((a,b))
lst.sort(key=lambda x:(x[0]))
answer=0
before=10*60

for a,b in lst:
    answer=max(answer,a-before)
    before=max(before,b)
answer=max(answer,22*60-before)
print(answer)