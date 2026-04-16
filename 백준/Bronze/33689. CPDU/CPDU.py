import sys
input=sys.stdin.readline
ans = 0
for _ in range(int(input())):
    s = input().rstrip()
    if s[0] == "C":
        ans+=1
print(ans)