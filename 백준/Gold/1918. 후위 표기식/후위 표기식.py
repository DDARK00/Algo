s = input()

s_priority = {"(": 0, "*": 2, "/": 2, '+': 1, '-': 1}
# 기본 우선순위
priority = {"(": 3, "*": 2, "/": 2, '+': 1, '-': 1}
# 스택 내부 우선순위

stack = []
answer = ''

for c in s:
    # print(stack)
    # print(answer)
    if c == ')':
        # 닫는 괄호-> 여는 괄호가 나올 때까지 다 뱉음
        while stack and stack[-1] != "(":
            answer += stack.pop()
        # print(stack)
        stack.pop()
    elif c in '+-/*(':
        if stack and s_priority[stack[-1]] < priority[c]:
            stack.append(c)
            # 기존에 있던 것보다 우선순위가 높다면 쌓음
            # 여는 괄호가 들어오면 -> 그냥 쌓음
            # 들어가 있는
            # 낮거나 같은게 들어오면 -> 뱉어냄

        elif stack and s_priority[stack[-1]] >= priority[c]:
            while stack and s_priority[stack[-1]] >= priority[c]:
                answer += stack.pop()

            stack.append(c)
        else:
            stack.append(c)
    else:
        answer += c
        # 입력값이 숫자(영어)면 더해줌
while stack:
    answer += stack.pop()
print(answer)