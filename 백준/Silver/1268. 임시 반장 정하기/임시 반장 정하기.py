import sys

input = sys.stdin.readline

n = int(input().strip())

cnt = [set() for i in range(n)]

# n명

lst = [list(map(int,input().split()))for _ in range(n)]

 # 5개씩 n명

for i in range(n):

    for j in range(5):

        for k in range(n):

            if lst[i][j] ==lst[k][j]:

                cnt[i].add(k)

lst = list(map(len,map(list,cnt)))

print(lst.index(max(lst))+1)