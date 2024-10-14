import sys
input=sys.stdin.readline

arr = []
a, *s = input().split()
a = int(a)
def rev(c):
    c = c[::-1]
    return int(c)

arr.extend(map(rev,s))

while True:
    ns = input().split()

    if len(arr) == a:
        break
    arr.extend(map(rev,ns))


print(*sorted(arr),sep='\n')