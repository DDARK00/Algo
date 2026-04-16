import sys
input=sys.stdin.readline
 
def solve(num):
    ans = (len(num)-1)*9+1 # (0 -> 1)
    ans += int(num[0])
    if int(num[0]*len(num)) > int(num):
        ans -=1
    
    return ans
print(solve(input().rstrip()))