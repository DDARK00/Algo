import sys
from collections import defaultdict
input=sys.stdin.readline


while True:
    n, m = map(int, input().split())
    score = defaultdict(int)
    if n == 0 and m==0:
        break
    for _ in range(n):
        for num in map(int,input().split()):
            score[num]+=1;
    target = set()
    ans = defaultdict(list)
    for idx, num in score.items():
        target.add(num)
        ans[num].append(idx)
    target = list(target)
    target.sort()
    print(*sorted(ans[target[-2]]))