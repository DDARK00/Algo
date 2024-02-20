import sys

input = sys.stdin.readline

while True:

    s = input()
    if s.rstrip() == '.':
        break

    stack = []
    throw = True
    for c in s:
        if c in ["(", "["]:
            stack.append(c)
        if c == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                throw = False
                break
        if c == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                throw = False
                break
    # print(stack)
    if throw and not stack:
        print('yes')
    else:
        print('no')
