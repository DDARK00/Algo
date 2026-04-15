import sys
input=sys.stdin.readline

for _ in range(int(input())):
    s1 = input().rstrip()
    s2 = input().rstrip()
    s1=s1.split(",")
    d={}
    for stat in s1:
        id, lv = stat.split(":")
        d[id]=int(lv)
    ans = 1e9
    s2=s2.split("|")
    for com in s2:
        t = 0
        for id in com.split("&"):
            t = max(t,d[id])
        ans = min(ans, t)

    print(ans)