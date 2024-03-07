import sys

input = sys.stdin.readline

t = int(input())


def search_friend(na: str):
    if tree.get(na):
        if tree[na][0] == na:
            return tree[na]
        tree[na] = search_friend(tree[na][0])
        return tree[na]
    else:
        tree[na] = (na, 1)
        return tree[na]
        # 들어온 이름, 친구의 수-> 혼자면 1명


for _ in range(t):
    f = int(input())
    # 친구의 관계 수
    tree = {}
    for _ in range(f):
        a, b = input().split()
        # a랑 b가 친구가 되었따
        a_f, a_cnt = search_friend(a)
        b_f, b_cnt = search_friend(b)
        # 각각 대표 친구 이름과 친구 수
        if a_f != b_f:
            # 둘이 친구가 아니었다면 union
            if a_cnt > b_cnt:
                # 큰게 작은거 밑으로 가자...
                tree[a] = (b_f, a_cnt + b_cnt)
                # tree[b] = (b_f,a_cnt+b_cnt)
                # 어차피 네임이 일치하지 않으면 cnt를 조회하지 않으니까 스킵

                tree[a_f] = (b_f, a_cnt + b_cnt)
                tree[b_f] = (b_f, a_cnt + b_cnt)

            else:
                # 반대로
                tree[b] = (a_f, a_cnt + b_cnt)
                tree[b_f] = (a_f, a_cnt + b_cnt)
                tree[a_f] = (a_f, a_cnt + b_cnt)
            print(a_cnt + b_cnt)
            # 친구가 아니었따면 합
        else:
            #친구였다면 기존의 합
            print(a_cnt)
