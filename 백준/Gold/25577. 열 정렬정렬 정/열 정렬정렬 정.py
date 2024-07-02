import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
# print(lst)

correct = sorted(lst)
# 중복 수가 있는가? 없다고 가정
keys = {}
for idx, c in enumerate(correct):
    keys[c] = idx
change = 0
for i in range(n):
    now = lst[i]
    right = keys[now]
    while i != right:
        change+=1
        lst[i], lst[right] = lst[right], lst[i]
        right = keys[lst[i]]
print(change)
# 그래서 이게 왜 맞는거임 증명을 못 하겠네 순사분이 뭐야