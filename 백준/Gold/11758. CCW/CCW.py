import sys

input = sys.stdin.readline

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

val = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
# 외적... 신발끈...공식...
if val < 0:

    print(-1)
elif val > 0:
    print(1)
else:
    print(0)
