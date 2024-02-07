import sys
n = int(sys.stdin.readline().rstrip())
# 다음 N개의 줄에는 숫자가 세 개씩 주어진다.

# maxdp
# dp[i][0] = max(dp[i-1][0], dp[i-1][1]) + lst[i][0]
# dp[i][1] = max(dp[i-1][0],max(dp[i-1][1],dp[i-1][2])) + lst[i][1]
# dp[i][2] = max(dp[i-1][1],dp[i-1][2]) + dp[i][2]
#
# mindp -> mindp


a, b, c = map(int, input().split())

max_a = a
max_b = b
max_c = c

min_a = a
min_b = b
min_c = c

# 인풋 받는 변수
for i in range(0, n -1):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    temp1 = max(max_a, max_b) + a
    temp2 = max(max_a, max_b, max_c) + b
    temp3 = max(max_b, max_c) + c

    max_a = temp1
    max_b = temp2
    max_c = temp3

    temp1 = min(min_a, min_b) + a
    temp2 = min(min_a, min_b, min_c) + b
    temp3 = min(min_b, min_c) + c

    min_a = temp1
    min_b = temp2
    min_c = temp3

print(max(max_a, max_b, max_c), min(min_a, min_b, min_c))

# 이번에도 터지면 드랍한다...
# 풀고 다른 풀이 찾아봤는데
# 배열은 한번에 초기화해도 계산 후에 값을 받아서 temp 안 만들어도 되는구나 배워갑니다~
