import sys

input = sys.stdin.readline

n, m = map(int, input().split())
# n개 m개중

lst = input().split()
lst.sort()

select = []

# print(lst)
lstone = ['a', 'e', 'i', 'o', 'u']


def dfs(k, p):
    if k == n:
        aeiou_cnt = 0
        else_cnt = 0
        for c in select:
            if c in lstone:
                aeiou_cnt +=1
            else:
                else_cnt+=1
        if aeiou_cnt>=1 and else_cnt>=2:

            print("".join(select))
        return

    for i in range(p, m):
        select.append(lst[i])
        dfs(k + 1, i + 1)
        select.pop()


dfs(0, 0)


