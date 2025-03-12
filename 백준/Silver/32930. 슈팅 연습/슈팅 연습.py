n,m = map(int,input().split())

lst = [tuple(map(int,input().split())) for _ in range(n)]

cx, cy = 0,0
ans = 0
for _ in range(m):
    lst.sort(key=lambda x:(cy-x[1])**2+(cx-x[0])**2)
    nx, ny = lst.pop()
    ans += (cx-nx)**2+(cy-ny)**2
    cx, cy = nx, ny
    lst.append(tuple(map(int,input().split())))
print(ans)