import sys

input = sys.stdin.readline

n,k,q = map(int,input().split())

# 사람 메세지 쿼리

# print(chr(65))

human = [chr(65+i) for i in range(n)]

lst = list(tuple(input().split()) for _ in range(k))

# print(lst)

human[0] = ""

for i in range(q-1,k):

    human[ord(lst[i][1])-65] = ""

target = lst[q-1][0]

for j in range(q-2,-1,-1):

    

    if lst[j][0] == target:

        human[ord(lst[j][1])-65] =""

    else:

        break

if lst[q-1][0] == '0' or not "".join(human):

    print(-1)

else:

    print(*list("".join(human)))

