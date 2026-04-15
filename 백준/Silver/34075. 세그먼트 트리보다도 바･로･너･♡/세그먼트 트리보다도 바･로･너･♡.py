import sys
input=sys.stdin.readline

n=int(input()) # algo
# 1~30
algo = []
for _ in range(n):
    id, tier = input().split()
    algo.append((id,int(tier)))
algo.sort(key=lambda x:(x[0])) # stable

n=int(input()) # idol
idol={}
for _ in range(n):
    id, tier = input().split()
    idol[id]=int(tier)

n=int(input()) # query
algo1, algo2="",""
for _ in range(n):
    query = input().rstrip()
    # print(query)
    if query == "nani ga suki?":
        print(f'{algo2[0]} yori mo {algo1[0]}')
    else:
        id, *query= query.split(" ")
        print("hai!")
        tier=idol[id]
        algo1, algo2, *_ = sorted(algo, key=lambda x:(abs(x[1]-tier)))