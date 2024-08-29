import sys

input = sys.stdin.readline

l = input().split()

ls = [

    int(l[0]+l[1]+l[2]+l[3]),

    int(l[1]+l[2]+l[3]+l[0]),

    int(l[2]+l[3]+l[0]+l[1]),

    int(l[3]+l[0]+l[1]+l[2]),

]

nums = set()

for i in range(1111,min(ls)):

    l = list(str(i))

    if "0" in l:

        continue

    val = [

    int(l[0]+l[1]+l[2]+l[3]),

    int(l[1]+l[2]+l[3]+l[0]),

    int(l[2]+l[3]+l[0]+l[1]),

    int(l[3]+l[0]+l[1]+l[2]),

    ]

    nums.add(min(val))

    

print(len(nums)+1)