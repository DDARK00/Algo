import sys

input = sys.stdin.readline

# 각 테스트 케이스는 짝수 정수 n 하나로 이루어져 있다. (6 ≤ n ≤ 1000000)

lst = [1] * 1000001
lst[1] = lst[0] = 0

for i in range(2, 1001):
    for j in range(i * 2, 1000001, i):
        lst[j] = 0

while True:
    n = int(input())
    if n == 0:
        break
    # a+b = n
    for i in range(3, n // 2 + 1, 2):
        # 하아... 문제 엄청 까다롭네...

        if lst[i] and lst[n - i]:
            print(f'{n} = {i} + {n - i}')
            break

    else:
        print("Goldbach's conjecture is wrong.")
