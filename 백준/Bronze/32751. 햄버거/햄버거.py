
n = int(input())
a, b, c, d = map(int, input().split())
s = input()
g = {"a":1,"b":0,"c":0,"d":0}
max = {"a":a,"b":b,"c":c,"d":d}
if s[0] != "a":
    print("No")
    exit()

before = "a"
for i in range(1,n):
    now = s[i]
    if now in "abcd" and before != now and g[now]<max[now]:
        before = now
        g[now]+=1
    else:
        print("No")
        exit()
if s[-1] == "a":
    print("Yes")
else:
    print("No")