import sys
s = sys.stdin.readline().rstrip()

ans = 0
temp = 0
while True:
    if len(s) == 1:
        break
    ans+=1
    for c in s:
        temp+= int(c)
    s = str(temp)
    temp = 0
print(ans)
print("YES" if s in ["3", "6", "9"] else "NO")