import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
# 점, 차례

p_list = [i for i in range(n)]


def search_p(item):
    p = p_list[item]
    if item != p:
        p = search_p(p)

    p_list[item] = p
    return p


def change_p(a, b):
    p1 = search_p(a)
    p2 = search_p(b)

    if p1 != p2:
        p_list[p2] = p1
        p_list[b] = p1
        return False
    else:
        return True


find = False
for i in range(m):
    a, b = map(int, input().split())
    rst = change_p(a, b)
    if rst:
        find = True
        print(i + 1)
        break

if not find:
    print(0)
