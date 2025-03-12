import sys
input = sys.stdin.readline

n, m = map(int, input().split())

one = list(map(int, input().split()))
two = list(map(int, input().split()))

one.sort(reverse=True) # earn
two.sort() # lost

a, b = 0, 0

ans = 0
while True:
    if a == n or b == m:
        break
    if one[a] - two[b] > 0 :
        ans+= one[a]-two[b]
    else:
        break
    a +=1
    b +=1
print(ans)