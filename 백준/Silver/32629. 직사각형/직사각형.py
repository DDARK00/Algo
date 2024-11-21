import sys, math
input=sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    l = math.floor(math.sqrt(n))
    rem = n-l**2
    add = math.ceil(rem/l)
    print(l*4+add*2)