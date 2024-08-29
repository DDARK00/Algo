import sys
import math

input = sys.stdin.readline

a, b  = map(int,input().split())

# a+1 ~ b

c = math.isqrt(b) - math.isqrt(a)

if c == 0:

    print(0)
    exit()

p = b-a
gcd = math.gcd(c,p)

print(f'{c//gcd}/{p//gcd}')

# 별 이상한 문제가 다 있네