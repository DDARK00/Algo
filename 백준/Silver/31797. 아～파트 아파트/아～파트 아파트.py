import sys

input = sys.stdin.readline

n, m = map(int,input().split())

# 아파트, 참가자

lst = [0]*10001

for i in range(1,m+1):

    a,b = map(int,input().split())

    lst[a], lst[b] = i, i

    # 높이가 순서대로가 아닐 수 있나?

lst = list(filter(lambda x: x>0,lst))

print(lst[n%(2*m)-1])