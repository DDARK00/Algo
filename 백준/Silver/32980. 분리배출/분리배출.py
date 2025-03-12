import sys
input=sys.stdin.readline

n=int(input())
gomi = [input().rstrip() for _ in range(n)]
P,C,V,S,G,F = map(int, input().split())
O = int(input())
money = {
    "P":P,"C":C,"V":V,"S":S,"G":G,"F":F,"O":O
}

ans = 0
for s in gomi:
    last = s[0]
    one = True
    for c in s:
        if c == last:
            continue
        else:
            one=False
            break
    if one:
        ans+= min(len(s)*money[last], len(s)*money["O"])
    else:
        ans+= len(s)*money["O"]
print(ans)