import sys

input = sys.stdin.readline

s = input().strip()

s = s.replace("()","+")

# print(s)

stack =[]

ans = 0

for c in s:

    if c =="(":

        stack.append("?")

    elif c ==")":

        stack.pop()

        ans+=1

    else:

        ans+=len(stack)

print(ans)