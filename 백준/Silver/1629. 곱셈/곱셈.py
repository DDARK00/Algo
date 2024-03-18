import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())


# a^b %c


def poweroverwhileming(n, s):
    if s == 1:
        return n % c
    if s % 2:
        k = poweroverwhileming(n, (s - 1) // 2)
        return (k * k * n) % c
    # 홀수면

    else:
        # 짝수면
        k = poweroverwhileming(n, s // 2)
        return (k * k) % c


# 분할 정복을 이용한 거듭제곱
# 10^11 = 10^2*10^2*10^2*10^2*10^2*10

# print(poweroverwhileming(a, b))

# 모듈러 연산을 어느 시점에서 해 줘야 하는걸까 모르겠다
print(pow(a, b, c))
