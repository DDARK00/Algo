h, m = map(int, input().split())
# 360 12 30
h%=30
if 30 * (m/360) == h:
    print("O")
else:
    print("X")