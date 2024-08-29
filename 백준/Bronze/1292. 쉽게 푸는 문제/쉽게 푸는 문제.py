import math
a, b = map(int, input().split())

# print(a,b)
# a 부터 b 까지

arr = [0]*(b+1)

p=1
v=1
c=0
# 1 2 2 3 3 3 4
# 1 3 5 8 11 14 18
while True:
    if len(arr) == p :
        break
    
    arr[p] = arr[p-1] + v;
    # 누적합
    p+=1
    c+=1
    if c== v:
        c= 0
        v += 1
# print(arr)
print(arr[b] - arr[a-1])