import sys
input=sys.stdin.readline

times=[
[390, 540],
[590, 600],
[650, 660],
[710, 720],
[770, 830],
[880, 890],
[940, 950],
[1000, 1370]]
a,b=input().split()
k=int(a)*60+int(b)
for s,e in times:
    if s<=k<=e:
        print('Yes')
        exit()
print('No')