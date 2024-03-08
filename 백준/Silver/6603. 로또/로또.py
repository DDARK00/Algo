import sys

input = sys.stdin.readline


def dfs(k):
    if len(select) == 6:
        print(*select)
        return

    for i in range(k, n):
        if lst[i] not in select:
            select.append(lst[i])
            dfs(i + 1)
            select.pop()


while True:
    st = input()
    if st.startswith("0"):
        break
    n, *lst = list(map(int, st.split()))

    select = []

    dfs(0)
    print()
