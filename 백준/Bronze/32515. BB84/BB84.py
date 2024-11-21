import sys
input = sys.stdin.readline

n = int(input())
js = input().rstrip()
jk = input().rstrip()

ss = input().rstrip()
sk = input().rstrip()

ans = ""
ok = True
for i in range(n):
    if js[i] == ss[i] :
        if jk[i] == sk[i]:
            ans += jk[i]
        else:
            ok = False
            break
if ok:
    print(ans)
else:
    print("htg!")