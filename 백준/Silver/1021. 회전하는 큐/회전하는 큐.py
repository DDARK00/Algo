from collections import deque

n, m = map(int, input().split())
# 첫째 줄에 큐의 크기 N과 뽑아내려고 하는 수의 개수 M이 주어진다.

deq = deque(i for i in range(1, n + 1))

# 첫 번째 원소를 뽑아낸다. 이 연산을 수행하면,
# 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.

target_list = map(int, input().split())
# m개
move_cnt = 0
for target in target_list:
    # 왼쪽, 오른쪽에서 가까우면 ~ reverse~
    distance = deq.index(target)
    reverse = False
    if distance > len(deq) - distance:
        distance = len(deq) - distance
        reverse = True
    # print(distance, reverse, target)
    if reverse:
        deq.rotate(distance)
        move_cnt += distance
    else:
        deq.rotate(-distance)
        move_cnt += distance
    deq.popleft()
    # 회전하는~~ 큐~~

print(move_cnt)
