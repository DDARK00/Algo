n, m, x, y = map(int, input().split())
_, s = input().split()
s=int(s)
lst=[]
for _ in range(n-1):
    a, b = input().split()
    if a.startswith("2024"):
        lst.append(int(b)+max(y-(x-int(b)),0))
if len(lst)<m:
    print("YES")
    print(0)
    exit()
lst.sort(reverse=True)
if lst[m-1]-s<=y:
    print("YES")
    print(max(0,lst[m-1]-s))
else:
    print("NO")