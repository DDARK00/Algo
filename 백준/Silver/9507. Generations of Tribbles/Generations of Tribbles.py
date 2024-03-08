import sys

input = sys.stdin.readline

T = int(input())
# 테케 수

k_fi = [1] * 68
# 0 ≤ n ≤ 67
k_fi[2] = 2
k_fi[3] = 4

for i in range(4, 68):
    k_fi[i] = k_fi[i - 1] + k_fi[i - 2] + k_fi[i - 3] + k_fi[i - 4]
# print(k_fi)

for t in range(1, T + 1):
    n = int(input())
    print(k_fi[n])
