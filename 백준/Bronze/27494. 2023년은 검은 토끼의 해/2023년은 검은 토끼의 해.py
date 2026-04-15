import sys
input=sys.stdin.readline
n=int(input())
if n<2023:
    print(0)
    exit()

answer=0
w="2023"
for i in range(2023, n+1):
    idx=0
    for c in str(i):
        if c==w[idx]:
            idx+=1
        if idx==4:
            answer+=1
            break
print(answer)