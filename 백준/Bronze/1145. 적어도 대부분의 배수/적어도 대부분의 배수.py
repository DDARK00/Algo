import sys
lst = list(map(int,sys.stdin.readline().split()))
k = min(lst)
while True:
    cnt=0
    for num in lst:
        cnt += k%num==0
    if cnt>=3:
        break
    k+=1
print(k)