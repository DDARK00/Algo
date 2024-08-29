import sys
# from collections import deque
input  = sys.stdin.readline

n, q = map(int, input().split())
# 수열 수 연산 수

na = list(map(int, input().split()))
# 수열

# 1더하기
# 2오른쪽
# 3왼쪽

# print(na)
# 연산하기
# 덱은 o[i] 조회가 최악 O(n)
# 리스트는 o(1)

# 돌리기를 안 돌리고 하기

index = 0
for _ in range(q):
    no, *order = input().split()
    # print(na, index)
    
    if no == '1':
        idx, k = order
        idx = (index + int(idx) - 1)%n
        na[idx]+=int(k)
        
    elif no == '2':
        index = (index +n - int(order[0]))%n
        
    elif no == '3':
        index = (index+int(order[0]))%n

# print(index,n)
for i in range(n):
    print(na[(i+index)%n], end=" ")