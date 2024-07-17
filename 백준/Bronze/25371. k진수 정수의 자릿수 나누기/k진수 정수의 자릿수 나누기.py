import sys
input = sys.stdin.readline

n, k = map(int,input().split())
# n->k
def dk(n, k):
    if n == 0:
        return "0"

    rst = ""
    while n > 0:
        rst = str(n%k) + rst
        n = n // k

    return rst
ans = 0
for el in dk(n,k).split("0"):
    if el.isdigit():
        ans+=int(el)
print(dk(ans,k))
# 이게정해야? 브1