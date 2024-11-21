import sys
from math import sqrt, floor
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    ans = ""
    if n%2 :
        ans+="O"
    if floor(sqrt(n)) ** 2 == n:
        ans += "S"
    
    if not ans:
        ans = "EMPTY"
    print(ans)