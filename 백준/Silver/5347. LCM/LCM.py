import sys

input = sys.stdin.readline


def getGCD(a, b):
    if b == 0:
        return a
    else:
        return getGCD(b, a % b)  # 유클리드 호제법


T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(a // getGCD(a, b) * b)
