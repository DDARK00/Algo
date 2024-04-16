import sys

input = sys.stdin.readline

n, d, k, c = map(int, input().split())
# 접시, 초밥, k개면 c를 준다

lst = [int(input()) for _ in range(n)]
lst = lst + lst[:]

visited = [0] * (d + 1)

slide = set(lst[:k])
slide.add(c)
for i in range(k):
    visited[lst[i]] += 1
max_len = len(slide)

for i in range(k, len(lst)):
    # print(i - k, i)
    visited[lst[i]] += 1
    slide.add(lst[i])
    visited[lst[i - k]] -= 1
    if not visited[lst[i - k]]:
        slide.discard(lst[i - k])
    slide.add(c)
    max_len = max(max_len, len(slide))

    # print(slide)
print(max_len)