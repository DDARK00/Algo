# 666 1666 9666 6660 6669
import sys
input = sys.stdin.readline
n = int(input())
names = []

i = 666
while len(names) < n:
    if '666' in str(i):
        names.append(i)
    i+=1
print(names[n-1])
 # 완전탐색 문제가 맞니...?