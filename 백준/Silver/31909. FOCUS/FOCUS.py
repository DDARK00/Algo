import sys
input = sys.stdin.readline
menu = [0]*256 # 0<=a<256

for i in range(0,8):
    a = 2**i
    for j in range(i+1, 8):
        b = 2**j
        menu[a+b] = (i,j) # 0<=i<j<=7

n = input()
lst = list(map(int,input().split()))
ans = int(input())
lst.reverse()
for num in lst:
    if menu[num] != 0:
        i, j = menu[num]
        if i == ans:
            ans = j
        elif j == ans:
            ans = i
print(ans)