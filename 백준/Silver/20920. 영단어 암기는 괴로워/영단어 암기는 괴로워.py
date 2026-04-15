import sys
from collections import defaultdict
input=sys.stdin.readline
n, m = map(int, input().split())

word = defaultdict(int)
for _ in range(n):
    if len(x:=input().rstrip())>=m:
        word[x]+=1

word = [(k, v) for k, v in word.items()]

for k, v in sorted(word, key=lambda x: (-x[1], -len(x[0]), x[0])):
    print(k)