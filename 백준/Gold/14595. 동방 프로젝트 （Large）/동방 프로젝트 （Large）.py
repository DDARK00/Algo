import sys

input = sys.stdin.readline

n = int(input())

# 동방 개수

lst = [0]*(n+1)

m = int(input())

# 행동 횟수

for _ in range(m):

    a, b = map(int,input().split())

    # a에서 b까지 뚫기

    lst[a] = max(lst[a], b)

    

end = 1

cnt = 0

for i in range(1, n+1):

    end = max(end, lst[i])

    

    if i >= end:

        cnt+=1

    # print(end, i, cnt)

print(cnt)

    