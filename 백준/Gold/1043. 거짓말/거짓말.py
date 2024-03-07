import sys

input = sys.stdin.readline

n, m = map(int, input().split())
# 사람 수, 파티 수

a, *b = map(int, input().split())
# 아는 사람 수, 번호 리스트
# 사람들의 번호는 1부터 N

a = int(a)

group = [i for i in range(n + 1)]


# print(b)


def chk_group(idx):
    if group[idx] == idx:
        return idx
    group[idx] = chk_group(group[idx])
    return group[idx]


if a > 0:
    target = b[0]
    for i in b:
        group[i] = target

        # 아는 사람을 한 그룹에 묶음
        # 아는 사람이 오는 파티 리스트라면
    ans = 0
    # print(group)
    party = []
    for _ in range(m):
        # 사람 수, 사람 번호
        # 여러 명이 오면 다 같은 트리로 때려박음
        a, *b = map(int, input().split())
        party.append(b)
        if len(b) > 1:

            q = chk_group(b[0])
            # b[0]의 부모 노드
            for i in range(1, len(b)):
                p = chk_group(b[i])
                # b[i]의 부모 노드

                group[b[i]] = q
                group[p] = q

                # 통일
        # 전처리 끝
    # print(party)
    know = chk_group(target)
    ans = 0
    for i in range(m):
        trust = False
        for h in party[i]:
            if chk_group(h) == know:
                trust = True
                break
        if not trust:
            ans += 1
    # print(group)
    # print(know)
    print(ans)
else:
    print(m)

# print(group)
