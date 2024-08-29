import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
lst = deque(lst)

minus = deque([])
while lst and lst[0]<0:
    minus.appendleft(-lst.popleft())

plus = lst
m_c = minus[-1] if minus else 0
p_c = plus[-1] if plus else 0

ans = 0

if m_c > p_c:
    cnt = 0

    if minus:
        ans += minus[-1]

    while minus and cnt<m:
        minus.pop()
        cnt+=1

else:
    if plus:
        ans += plus[-1]

    cnt = 0
    while plus and cnt<m:
        plus.pop()
        cnt+=1

while minus:
    ans += minus[-1]*2
    cnt = 0

    while minus and cnt<m:
        minus.pop()
        cnt+=1

while plus:
    ans += plus[-1]*2
    cnt = 0

    while plus and cnt<m:
        cnt+=1
        plus.pop()

print(ans)