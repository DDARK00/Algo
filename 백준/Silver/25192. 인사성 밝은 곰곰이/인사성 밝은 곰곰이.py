import sys

input = sys.stdin.readline

n = int(input())

ans = 0

temp = set()

for _ in range(n):

    tx = input().rstrip()

    if tx == "ENTER":

        ans+=len(temp)

        temp = set()

    else:

        temp.add(tx)

print(ans+len(temp))