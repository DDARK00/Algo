import sys
input=sys.stdin.readline

n, j, s, h, k = map(int, input().split())

lst = [input().rstrip() for _ in range(3)]
p=[0]*3 # 낮 높 상

th = {
    "^":1, # 높
    "v":2 # 상
}
# w jump slide hp -k
for i in range(n):
    if lst[1][i] != ".":
        p[th[lst[1][i]]]+=1
    elif lst[2][i]!=".":
        p[0]+=1

p[2]=max(p[2]-s,0)
p[1]=max(0, p[1]-max(0, j-p[0])//2)
p[0]=max(0,p[0]-j)

damage = sum(p)*k
print(-1 if h-damage<=0 else h-damage)