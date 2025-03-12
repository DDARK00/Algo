import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())
A = list(map(int, input().split()))

lp = A[:l-1]
mp = A[l-1:r]
rp = A[r:]
# print(lp,mp,rp)

ismono = True
if lp:
    mx = max(lp)
    mn = min(mp)
    if mx>mn:
        ismono = False

if rp:
    mx = max(mp)
    mn = min(rp)
    if mx>mn:
        ismono = False

if ismono:
    print(1)
else:
    print(0)