import sys
input=sys.stdin.readline

def solve():
    nums=[0]+list(map(int,input().split()))
    nums[9]+=nums[6]
    nums[6]=0

    n=sum(nums)
    answer=[0]*n

    idx=9
    k=0
    while n>k:
        if nums[idx]>0:
            answer[-1-(k//2) if k%2 else (k//2)]=idx
            nums[idx]-=1
            k+=1
        else:
            idx-=1

    print(*answer)
for _ in range(int(input())):
    solve()