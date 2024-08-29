import sys
input = sys.stdin.readline

s = input().rstrip()


cnt = 0
ans = ""
for c in s:
    if c != ".":
        cnt+=1
    else:
        if cnt%2 == 1:
            ans = -1
            break
        else:
            while cnt != 0 and cnt>=4:
                ans+="AAAA"
                cnt-=4
            if cnt == 2:
                ans+="BB"
                cnt-=2
        ans+="."
if cnt %2 == 1:
    ans = -1
else:
    while cnt != 0 and cnt>=4:
        ans+="AAAA"
        cnt-=4
    if cnt == 2:
        ans+="BB"
        cnt-=2
print(ans)