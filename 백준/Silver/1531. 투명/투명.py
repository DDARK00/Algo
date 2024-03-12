import sys

input = sys.stdin.readline

n, m = map(int, input().split())
# n개로 가리는데 m개는 붙여야 가려짐

# 모자이크한 100×100크기의 그림

img = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(n):
    sx, sy, ex, ey = map(int, input().split())
    for i in range(sx-1, ex):
        for j in range(sy-1, ey):
            img[i][j] += 1

cnt = 0
for i in range(100):
    for j in range(100):
        if m < img[i][j]:
            cnt += 1
print(cnt)
# print(img)
