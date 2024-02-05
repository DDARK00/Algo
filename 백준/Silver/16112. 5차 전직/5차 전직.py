# sort 해서 앞에서부터 깐다

# n 개
# k -1 까지는 반감
n, k = map(int, input().split())

lst = list(map(int,input().split()))

s=0
lst.sort()

for idx, v in enumerate(lst):
    if idx<k :
        s += (idx )* v
    else:
        s += k * v
print(s)