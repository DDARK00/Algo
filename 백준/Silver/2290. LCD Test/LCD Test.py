import sys
input=sys.stdin.readline

s, n = input().split() # 10, 10e10
s=int(s)
n = list(map(int,list(n)))
# s+2 m
# 2s+3 n

l = "|"+" "*s+" " # 1
r = " "+" "*s+"|" # 2
lr = "|"+" "*s+"|" # 3
tb = " "+"-"*s+" " # 4
blank = " "+" "*s+" " # 5
g = [
    [tb, lr, blank, lr, tb],
    ["  "+" "*s," "*s + " |", "  "+" "*s," "*s+" |", "  "+" "*s],
    [tb, r, tb, l, tb],
    [tb, r, tb, r, tb],
    [blank, lr, tb, r, blank],
    [tb, l, tb, r, tb],
    [tb, l, tb, lr, tb],
    [tb, r, blank, r, blank],
    [tb, lr, tb, lr, tb],
    [tb, lr, tb, r, tb]
]

for num in n:
    print(g[num][0], end=" ") #1
print()
for _ in range(s):
    for num in n:
        print(g[num][1],end=" ") #2
    print()
for num in n:
    print(g[num][2], end=" ") #3
print()
for _ in range(s):
    for num in n:
        print(g[num][3],end=" ") #4
    print()
for num in n:
    print(g[num][4], end=" ") #5
print()