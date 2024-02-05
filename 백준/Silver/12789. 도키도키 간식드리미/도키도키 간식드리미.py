n = int(input())

stack = []

lst = list(map(int, input().split()))
# 현재 줄 선 순서
lst.reverse()
target = 1
while lst:
    if lst[-1] == target:
        target += 1
        lst.pop()
    else:
        if stack and stack[-1] == target:
            stack.pop()
            target += 1
        else:
            stack.append(lst.pop())
# 일단 스택에 다 때려박고 나오는 게 없으면 새드~


while stack:
    if stack[-1] == target:
        stack.pop()
        target += 1
    else:
        break

if stack:
    print('Sad')
else:
    print('Nice')
