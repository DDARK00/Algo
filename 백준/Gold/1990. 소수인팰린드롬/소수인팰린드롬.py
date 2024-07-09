import sys
import math
input = sys.stdin.readline
a, b = map(int, input().split())
# 루트1억 1초
if b > 10000000:
    b = 9999999
    # 이게 어렵다 1억이면 9자리 8자리 안되는구나ㅇ
lst = []
start = 101 if a < 101 else (a + (0 if a%2 else 1))
if a<=5 and b>=5:
    lst.append(5)
if a<=7 and b>=7:
    lst.append(7)
if a<=11 and b>=11:
    lst.append(11)

for i in range(start,b+1,2):
    num = str(i)
    if len(num)%2 and num == num[::-1]:
        lst.append(i)

for num in lst:
    find = True
    end = int(math.sqrt(num))+1
    for i in range(2,end):
        if num%i == 0:
            find = False
            break
    if find:
        print(num)
print(-1)