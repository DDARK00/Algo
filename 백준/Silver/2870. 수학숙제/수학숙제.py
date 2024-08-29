import sys
import re
input = sys.stdin.readline

n = int(input())
regex = r'[0-9]+'
lst = []
for _ in range(n):
    s = input().rstrip()
    lst.extend(map(int,re.findall(regex,s)))
lst.sort()
print(*lst, sep='\n')