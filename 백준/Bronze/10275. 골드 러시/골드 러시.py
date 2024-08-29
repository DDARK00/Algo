import sys
input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    n, a, b = map(int, input().split())
    # a+b=2^n
    if a%2 == 1:
        print(n)
    else:
        k = min(a, b)
        cnt = 0
        while (k&1) != 1:
            k=k>>1
            cnt+=1
        print(n-cnt)