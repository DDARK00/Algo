import sys
input=sys.stdin.readline
_, k = map(int,input().split())
for idx, num in enumerate(map(int,input().split())):
    if idx!=num and abs(idx-num)%k !=0:
        print("No")
        exit(0)
print("Yes")