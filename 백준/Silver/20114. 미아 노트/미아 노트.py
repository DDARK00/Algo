import sys
input=sys.stdin.readline

n, h, w = map(int, input().split())

blur = [input().rstrip() for _ in range(h)]
ans = ["?"]*n

for i in range(n):
    for j in range(h):
        for k in range(w):
            target = blur[j][k+i*w]
            if target != "?":
                ans[i] = target
            if ans[i] != "?":
                break
        if ans[i] != "?":
            break
print("".join(ans))