import sys
input = sys.stdin.readline
n = int(input())
a_list = [int(input()) for _ in range(n)]
b_list = [int(input()) for _ in range(n)]
a_list.sort()
b_list.sort()
ans = 0
for i in range(n):
    ans += abs(a_list[i]-b_list[i])
print(ans)
# 이거 증명한거 예전에 어디서 봤는데 기억이 안 나냐..