import sys, math
input = sys.stdin.readline

s = int(input())

target = math.ceil(math.sqrt(s))
if target**2<s:
    print(target+1)
else:
    print(target)