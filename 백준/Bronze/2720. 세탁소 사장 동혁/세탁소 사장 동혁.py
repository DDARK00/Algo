import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):

    c = int(input())

    one = c//25

    c %=25

    two = c//10

    c %=10

    thr = c//5

    c%=5

    print(one, two, thr, c)