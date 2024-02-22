import sys

input = sys.stdin.readline

n = int(input())
con = []

for _ in range(n):
    con.append(list(map(int, input().split())))

con.sort(key=lambda x: (x[1],x[0]))
# print(con)

start = 0
cnt = 0

# lst = []
for s, e in con:
    if s >= start:
        cnt += 1
        # lst.append((s,e))
        start = e

print(cnt)
# print(lst)
