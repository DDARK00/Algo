import sys
input = sys.stdin.readline
n = int(input())
s = input().rstrip()

ans = ""
for c in s:
    if c == "4" or c == "5" :
        if len(ans)>1 and ans[-1] == "S" and ans[-2] == "P":
            continue
    ans+=c
print(ans)