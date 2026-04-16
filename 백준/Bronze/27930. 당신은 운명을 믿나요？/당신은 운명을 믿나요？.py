import sys
input = sys.stdin.readline

a = list("IESNOY")
b = list("AEROK")
s = input()

for c in s:
    if c == a[-1]:
        a.pop()
    if c == b[-1]:
        b.pop()
    if not a:
        print("YONSEI")
        break
    elif not b:
        print("KOREA")
        break