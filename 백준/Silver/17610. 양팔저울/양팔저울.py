import sys

input = sys.stdin.readline

k = int(input())

lst = list(map(int, input().split()))

ans = set()


def diff(left, right):
    ans.add(abs(left - right))


def sp(idx, left, right):
    if idx == k:
        diff(left, right)
        return
    # for i in range(idx, k):
    sp(idx + 1, left, right)
    sp(idx + 1, left + lst[idx], right)
    sp(idx + 1, left, right + lst[idx])


sp(0, 0, 0)
ans.discard(0)
# print(len(ans))
print(sum(lst) - len(ans))
# 추의 개수를 나타내는 정수 k(3 ≤ k ≤ 13)가 주어진다.
# 다음 줄에는 k개의 정수 gi(1 ≤ gi ≤ 200,000)가 공백으로 구분되어 주어지는데
# 와 너무 어렵다...
# 허