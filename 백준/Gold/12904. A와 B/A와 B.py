import sys
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()
# 뒤가 A일때 B일때

while len(t)>len(s):
    if t[-1] =="A":
        t = t[:-1]
    else:
        t = t[-2::-1]
if s==t:
    print(1)
else:
    print(0)