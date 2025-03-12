import sys
input=sys.stdin.readline

n=int(input())
key = [(1, 3), (1, 4), (3, 4)]
ins = [tuple(sorted(map(int, input().split()))) for _ in range(3)]
ins.sort()
if n == 3 and key==ins :
    print("Wa-pa-pa-pa-pa-pa-pow!")
else:
    print("Woof-meow-tweet-squeek")