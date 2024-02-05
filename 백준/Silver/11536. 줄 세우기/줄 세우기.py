n = int(input())

lst = ['s'] * n

for i in range(n):
    lst[i] = input()

a_lst = sorted(lst)
d_lst = sorted(lst, reverse=1)


sort_type = 'NEITHER'
if a_lst[0] == lst[0]:
    sort_type = 'INCREASING'

    for idx in range(1, len(lst)):
        if lst[idx] != a_lst[idx]:
            sort_type = 'NEITHER'
            break

elif d_lst[0] == lst[0]:
    sort_type = 'DECREASING'
    for idx in range(1, len(lst)):
        if lst[idx] != d_lst[idx]:
            sort_type = 'NEITHER'
            break

print(sort_type)