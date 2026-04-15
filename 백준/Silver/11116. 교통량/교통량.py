import sys;input=sys.stdin.readline
from collections import defaultdict
for _ in range(int(input())):
    l=defaultdict(int)
    r=defaultdict(int)
    m=int(input())
    for num in map(int,input().split()):
        l[num]=1
    for num in map(int,input().split()):
        r[num]=1

    ans=0
    for num in list(l.keys()):
        if l[num+500] and r[num+1000] and r[num+1500]:
            ans +=1
    print(ans)
'''
왼쪽 줄 위로 앞 바퀴가 지나 간 시간 t
왼쪽 줄 위로 뒷 바퀴가 지나 간 시간 t + 500
오른쪽 줄 위로 앞 바퀴가 지나 간 시간 t + 1000
오른쪽 줄 위로 뒷 바퀴가 지나 간 시간 t + 1500
'''