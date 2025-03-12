import sys
input=sys.stdin.readline

s=input().rstrip()
k=input().rstrip()

ans = 0
i = 0
while i<= len(s)-len(k):
    if s[i] == k[0]:
        isFinish=True
        for idx, c in enumerate(k):
            if s[i+idx] != c:
                isFinish = False
                break
        if isFinish:
            ans+=1
            i+=idx
    i+=1
print(ans)