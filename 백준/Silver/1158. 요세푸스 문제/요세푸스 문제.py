import sys

input = sys.stdin.readline

n, k = map(int, input().split())

# n번까지 k명


lst = list(range(1, n + 1))

print("<", end="")
ans = ""
pointer = k - 1

for i in range(n):
    # print(pointer)
    ans += str(lst.pop(pointer)) + ", "
    if not len(lst):
        break
    pointer = pointer + k - 1 if pointer + k - 1 < len(lst) else (pointer + k - 1) % len(lst)
print(ans[0:-2], end="")
print(">")
