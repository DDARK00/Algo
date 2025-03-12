a,b=map(int,input().split())

target = a
cnt = 0
while target>=b:
    target-=b
    cnt+=1
print(cnt,".",sep="",end="")
target*=10
for _ in range(1001):
    if target == 0:
        break
    cnt=0
    while target>=b:
        target-=b
        cnt+=1
    target*=10
    print(cnt,end="")