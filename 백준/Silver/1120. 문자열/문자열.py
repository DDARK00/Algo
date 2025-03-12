import sys
a, b = sys.stdin.readline().split()

# a<=b
ans = 51
for i in range(len(b)-len(a)+1):
    cnt = 0
    for idx, c in enumerate(a):
        if b[idx+i] != c:
            cnt+=1
            if cnt>=ans:
                break
    ans = min(ans, cnt)
print(ans)