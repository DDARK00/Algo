import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst = [(lst[i]-1, i)for i in range(n)]
lst.sort()

for k, l in lst:
    print(k-l)