a, b = map(int,input().split())
lst = [abs(b-a)] + [abs(b-int(input()))+1 for _ in range(int(input()))]
lst.sort()
print(lst[0])