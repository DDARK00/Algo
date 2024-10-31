import sys
input = sys.stdin.readline

n, m = map(int, input().split())

before = [list(map(int, list(input().rstrip()))) for _ in range(n)]
after = [list(map(int, list(input().rstrip()))) for _ in range(n)]
# print(before)

if n<3 or m<3:
    for i in range(n):
        for j in range(m):
            if before[i][j] != after[i][j]:
                print(-1)
                exit()
    print(0)
    exit()

ans = 0

for i in range(n-2):
    for j in range(m-2):
        if before[i][j] != after[i][j]:
            ans+=1
            for a in range(3):
                for b in range(3):
                    before[i+a][j+b] = abs(before[i+a][j+b]-1)
chk = True
for k in range(n):
    for l in range(m):
        if before[k][l] != after[k][l]:
            chk = False
            break

if chk:
    print(ans)
else:
    print(-1)