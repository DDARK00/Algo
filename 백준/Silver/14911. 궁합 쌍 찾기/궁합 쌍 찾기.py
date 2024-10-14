import sys
input = sys.stdin.readline

lst = list(map(int, input().split()))
lst.sort()
x = int(input())

s = set()
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        a = lst[i]
        b = lst[j]
        if a+b == x:
            s.add((min(a, b),max(a, b)))
        elif a+b>x:
            break
ans = list(s)
for a, b in ans:
    print(a, b)
print(len(ans))