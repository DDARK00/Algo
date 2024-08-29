import sys

input = sys.stdin.readline

n = int(input())

stack =[]

rst = []

s_lst = [int(input().rstrip()) for _ in range(n)]

s_lst.reverse()

for i in range(1,n+1):

    stack.append(i)

    rst.append("+")

    while s_lst and stack and stack[-1] == s_lst[-1]:

        stack.pop()

        s_lst.pop()

        rst.append('-')

        

# print(s_lst)

# print(rst)

if not s_lst and not stack:

    for oper in rst:

        print(oper)

else:

    print("NO")