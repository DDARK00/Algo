n = int(input())
# n일 동안의 일정

sch = [(1001, 0)] * (n + 1)
# 1일부터 N일까지 순서대로 주어진다. (1 ≤ Ti ≤ 5, 1 ≤ Pi ≤ 1,000)

for i in range(1, n + 1):
    sch[i] = tuple(map(int, input().split()))
# print(sch)

dp = [0] * (n + 1)
# 0일차는 0


lst = [[] for _ in range(n + 1)]
# 1일에 끝난 작업까지의 최대 + 1일에 고르는 작업(작업이 n일 이전에 끝난다면)
for idx, val in enumerate(sch):
    a, b = val
    # 기간, 돈 idx는 일자
    # 2일 시작에 1일 걸린다 -> 2일에 끝남
    if idx + a - 1 <= n:
        lst[idx + a - 1].append((idx, b))  # 걸리는 기간과 받는 돈, 보낼 곳/받을 곳
# print(lst)

# for i in range()

for i in range(1, n + 1):
    if not lst[i]:
        dp[i] = dp[i - 1]
    else:
        maximum = -1
        for a, b in lst[i]:  # 언제 시작했나, 얼마 받나
            maximum = max(maximum, dp[a - 1] + b,dp[i-1])  # 해당 작업을 완료한 돈+ 작업 시작 전날까지의 돈, or 오늘 놀고 어제까지의 돈
        dp[i] = maximum
print(dp[-1])
# print(dp)
