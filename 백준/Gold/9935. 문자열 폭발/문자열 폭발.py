import sys

input = sys.stdin.readline

stack = []

s = input().strip()

bomb = input().strip()

keyword = bomb[-1]

l = len(bomb)

for c in s:

    stack.append(c) 

    if c == keyword: 

        

        if len(stack) < l:

            continue

        d = True

        for i in range(1,l+1):

            if stack[-i] != bomb[-i]:

                d = False 

                break       

        if d:

            for _ in range(l):

                stack.pop()

if stack:

    print("".join(stack))

else:

    print("FRULA")  