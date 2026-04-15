import sys
from collections import defaultdict as dd
g=dd(int)
while True:
    s=sys.stdin.readline().split()
    if not s:
        break
    for c in s:
        g[c]+=1
total=sum(g.values())

for c in ['Re','Pt','Cc','Ea','Tb','Cm','Ex']:
    print(f'{c} {g[c]} {g[c]/total:.2f}')
print(f'Total {total} 1.00')