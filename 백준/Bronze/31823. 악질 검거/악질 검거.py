import sys

input = sys.stdin.readline

n, m = map(int,input().split())

# 인수 활동일

ans  = set()

lst = []

for _ in range(n):

    stric = 0

    m_s = 0

    target = input().split()

    for i in range(m):

        if target[i] == ".":

            stric += 1

            m_s = max(stric, m_s)

        else:

            stric = 0

    lst.append((m_s, target[-1]))

    ans.add(m_s)

print(len(ans))

list(map(lambda x: print(*x),lst))