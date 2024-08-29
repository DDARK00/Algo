import sys
input = sys.stdin.readline
N = input().rstrip()
F = int(input())

min = None
head = N[0:-2]

def create(k):
    k = str(k)
    if len(k) == 1:
        k = '0'+k
    return k

def mod(h,b):
    i = int(h+b)
    if i%F == 0:
        print(b)
        return True

for i in range(100):
    body = create(i)
    if mod(head,body):
        break
# 브론즈가 좀 하드하다?