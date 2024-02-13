from collections import deque

n = int(input())
lst = deque(list(range(1, n + 1)))

length = n

while length > 1:
    lst.popleft()
    length -= 1
    lst.rotate(-1)

print(lst[0])
