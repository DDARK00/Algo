import sys;input=sys.stdin.readline

k, d = map(int, input().split())

lst=[]
lst.append(k)
while lst[-1]*2+lst[0]<=d:
    lst.append(lst[-1]*2+lst[0])
print(len(lst))