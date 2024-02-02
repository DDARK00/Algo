import sys
input = sys.stdin.readline
T = int(input())

# 위치가 같은 두 점은 없다.

obj = {}
for i in range(T):
    x, y = map(int, input().split())
    # {y: [x1,x2,x3,x4]}
    if obj.get(y):
        obj[y].append(x)
    else:
        obj[y] = [x]

    #  좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬
#  N (1 ≤ N ≤ 100,000)이 주어진다.
#  (-100,000 ≤ xi, yi ≤ 100,000) 좌표

# 10만 + 20만 + 그밖의 계산시간
idx = -100000
while idx < 100001:
    if obj.get(idx):
        lst = obj[idx]
        lst.sort()
        while lst:
            print(lst.pop(0), idx)
    idx += 1

