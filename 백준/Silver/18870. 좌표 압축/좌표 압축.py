import sys

n = int(input().strip())
# 1 ≤ N ≤ 1,000,000
lst = input().strip().split()

s_lst = sorted(list(map(int, lst)))


idx = 0
prime = {}

for num in s_lst:
    num = str(num)
    if not prime.get(num):
        # 숫자가 이미 등록되어 있으면 암것두 안 해도 되지?
        prime[num] = str(idx)
        # print(idx,num)
        idx+=1

for s in lst:
    print(prime[s], end=" ")
# print()

# print(prime)
# print(s_lst)
# int str쪽 어떻게 절약 가능해 보임