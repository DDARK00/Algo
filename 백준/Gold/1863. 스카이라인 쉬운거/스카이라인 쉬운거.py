import sys

input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n):
    a, b = map(int, input().split())
    lst.append(b)
m = []
cnt = 0

# 같은게 들어오면 같은 층
# 더 큰게 들어오면 윗층
# 더 작은게 들어왔을 때 배열에 같은 값이 없다면 +1
# 하고 값 뱉기
# 0이면 건물이 아니니까 뱉기는 하는데 추가x
for x in lst:
    if m:
        while m and m[-1] > x:
            m.pop()
            cnt += 1
        if x != 0:
            if not m or m[-1] < x:
                m.append(x)
        # 같으면 아무것도 안 함

    else:
        m.append(x)

while m:
    if m.pop() != 0:
        cnt += 1
print(cnt)