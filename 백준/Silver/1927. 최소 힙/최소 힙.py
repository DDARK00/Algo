# import sys
# import heapq
#
# input = sys.stdin.readline
# lst = []
#
# n = int(input())
#
# for _ in range(n):
#     k = input().rstrip()
#     # print(lst, k)
#     # print(k == '0')
#     if k == '0':
#         if not lst:
#             print(0)
#         else:
#             print(heapq.heappop(lst))
#     else:
#         heapq.heappush(lst, int(k))
import sys

input = sys.stdin.readline
# 완전이진트리

n = int(input())

tree = [0] * (n + 1)
last = 0

for _ in range(n):
    k = input().rstrip()
    if k == '0':
        if last < 1:
            print(0)
        else:
            print(tree[1])
            tree[1] = tree[last]
            # 이쪽이 헷갈리네 일단 해본다
            last -= 1

            p = 1
            c = p * 2
            # 자식들보다 크면 -> 스왑

            while c <= last:
                if c + 1 <= last and tree[c] > tree[c + 1]:
                    # 적게 돌린다 -> 우측변을 탄다? 잘 모르겠다 일단 해본다
                    # 최소 힙이라서 둘 중 작은 쪽과 비교해서 작으면 스왑한다
                    # 트리의 부모는(양 차일드의 부모) 항상 차일드보다 작아야 한다.
                    c += 1

                if tree[p] > tree[c]:
                    tree[p], tree[c] = tree[c], tree[p]
                    # 더 작으면? 스왑
                    p = c
                    c = p * 2
                else:
                    break

            # print(tree)

    else:
        last += 1
        tree[last] = int(k)

        p = last // 2
        c = last
        # 부모, 자식

        while p > 0:
            if tree[p] > tree[c]:
                # 최소 힙
                tree[p], tree[c] = tree[c], tree[p]
                c = p
                p = c // 2
            else:
                break
# print(tree, last)
# 와 근데 손으로 짜니까 속도 개박살나네?