import sys
input = sys.stdin.readline
n, l, h = map(int,input().split())

lst = list(map(int,input().split()))
lst.sort()
print(sum(lst[l:n-h])/(n-l-h))