import sys
from collections import deque
input=sys.stdin.readline

input()
dq=deque(list(map(lambda x:(x[0]+1, int(x[1])),enumerate(input().split()))))

while dq:
    idx,val=dq[0]
    dq.popleft()
    print(idx, end=" ")
    
    if dq:
        dq.rotate(-(val-1) if val>0 else -val)
