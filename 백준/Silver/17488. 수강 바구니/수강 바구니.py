import sys
input=sys.stdin.readline

n, m = map(int, input().split())
l = list(map(int, input().split()))

bucket = [[0,[]] for _ in range(m+1)]

def add(sub, i):
    bucket[sub][0]+=1
    bucket[sub][1].append(i)

for i in range(n):
    for sub in map(int, input().split()):
        if sub == -1:
            break
        add(sub, i)
ans = {}
def conf():
    for idx in range(1, m+1):
        cnt, people = bucket[idx][0], bucket[idx][1]
        if l[idx-1]>=cnt:
            l[idx-1]-=cnt
            for num in people:
                if ans.get(num):
                    ans[num].append(idx)
                else:
                    ans[num] = [idx]
        else:
            l[idx-1] = 0
        bucket[idx][0] = 0
        bucket[idx][1] = []
conf()
for i in range(n):
    for sub in map(int, input().split()):
        if sub == -1:
            break
        add(sub, i)
conf()
for i in range(n):
    if ans.get(i):
        print(*sorted(ans[i]))
    else:
        print("망했어요")