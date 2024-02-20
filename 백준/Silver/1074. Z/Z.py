import sys

input = sys.stdin.readline
# 첫째 줄에 정수 N, r, c가 주어진다.

n, r, c = map(int, input().split())


# 가로 2**n, 세로 2**n

def half(i, j, flag, msum):
    if flag > 1:
        h = 2 ** (flag - 1)
        # print(2*h*2*h)
        # print(i, j, msum, "-------------")  # 3 ,1
        # print(i-h, j-h, r,c)
        if i - h > r and j - h > c:
            half(i - h, j - h, flag - 1, msum)
        elif i - h > r and j - h <= c:
            half(i - h, j, flag - 1, msum + (2 * h * 2 * h) // 4 * 1)
        elif i - h <= r and j - h > c:
            half(i, j - h, flag - 1, msum + (2 * h * 2 * h) // 4 * 2)
        else:
            half(i, j, flag - 1, msum + (2 * h * 2 * h) // 4 * 3)
    else:
        # print(msum)
        # print(i - 2, j - 2)
        # print(r, c)
        # print(msum)
        for k in range(i - 2, i):
            for l in range(j - 2, j):
                obj[(k, l)] = msum + 1
                msum += 1
        # print(msum)


# 2,2 면 2 2 4,4에 들어가야 하니까 미포함

# 2**i + 2*j
k = 0
# lst = [[0 for _ in range(2 ** n)] for _ in range(2 ** n)]
obj = {}

half(2 ** n, 2 ** n, n, 0)
# print(obj)
print(obj[(r, c)] - 1)
# print(lst[r])
# 하아 너무 힘들다 브루트포스 돌리는게 2시간, 시간초과로 아이디어 생각하는게 1시간, 그거 구현하는게 2시간...
