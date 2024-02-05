n =int(input())
# 스위치 개수, 100 이하의 양의 정수

lst=[0]
lst.extend(list(map(int, input().split())))
# 스위치

k = int(input())
# 학생 수

def man(order,s_list):
    # print(s_list)
    #자기가 받은 수의 배수를 바꾼다
    n_order= order
    while n_order<len(s_list):
        s_list[n_order] = 1 if s_list[n_order]== 0 else 0
        n_order+=order
    return s_list

def woman(order, s_list):
    # print(s_list,order)
    # 자기 수를 중심으로 대칭 비교
    s_list[order] = 1 if s_list[order] == 0 else 0
    idx = 1
    while 1<= order-idx and order+idx<len(s_list):
        if s_list[order-idx] == s_list[order+idx]:
            s_list[order-idx] = s_list[order+idx] = 1 if s_list[order-idx] == 0 else 0
            idx += 1
        else:
            break
    
    return s_list

for i in range(k):
    s, order = map(int, input().split())
    if s == 1:
        lst = man(order, lst)
    else:
        lst = woman(order,lst)


# 20개씩 출력

# n이20보다 크면 다음줄

# print(lst[1:20])
# print(lst[21:])

lst = lst[1:]
while len(lst)>20:
    for i in range(20):
        print(lst[i], end=" ")
    lst = lst[20:]
    print()

for i in lst:
    print(i, end=" ")
