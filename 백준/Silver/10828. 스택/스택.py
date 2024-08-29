import sys

input = sys.stdin.readline

n= int(input())

# 오더 수

stack = []

for _ in range(n):

    order, *k = input().split()

    

    # print(order, k)

    if order == 'push':

        stack.append(k[0])

    elif order == 'pop':

        if stack:

            print(stack.pop())

        else:

            print(-1)

    elif order == 'top':

        if stack:

            print(stack[-1])

        else:

            print(-1)

    elif order == 'size':

        print(len(stack))

    elif order == 'empty':

        if stack:

            print(0)

        else:

            print(1)