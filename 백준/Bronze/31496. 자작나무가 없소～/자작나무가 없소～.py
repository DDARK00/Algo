import sys
input=sys.stdin.readline

n, s=input().rstrip().split()
answer=0
for _ in range(int(n)):
    i,q=input().rstrip().split()
    for nm in i.split("_"):
        if nm==s:
            answer+=int(q)
            break
print(answer)