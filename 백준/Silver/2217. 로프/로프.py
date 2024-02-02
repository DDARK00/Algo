n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

lst.sort(reverse=1)

max_k = lst[0]
for i in range(1, n):
    if lst[i]*(i+1) >= max_k:
        max_k = lst[i]*(i+1)
    else:
        continue
        # 그리디
        # 튼튼한 것부터 집어서 계산...???

print(max_k)