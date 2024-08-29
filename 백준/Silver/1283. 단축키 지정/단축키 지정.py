n = int(input())

ans = []

sc = {}

for _ in range(n):

    origin = input()

    s = origin.split()

    # print(s)

    

    

    target = ""

    for i in range(len(s)):

        target+= s[i][0]

        #첫글자

    # 왼쪽부터 차례대로 -> 그냥 탐색

    target+= "".join(s)

    # 첫글자 중복 상관없지?

    idx =0

    while idx<len(target):

        c = target[idx]

        if not sc.get(c):

            sc[c.upper()]=1

            sc[c.lower()]=1

            if idx < len(s):

                # 앞글자

                st = "["+c+"]"+s[idx][1:]

            

                s[idx] = st

                ans.append(" ".join(s))

            else:

                #안에 글자

                # print(c)

                # 여기로 들어왔다 -> 밖에서 안 쓰고 왔다

                oi = origin.index(c)

                ans.append(origin[:oi]+"["+c+"]"+origin[oi+1:])

            

            break

        idx +=1

        if idx ==len(target):

            ans.append(origin)

for a in ans:

    print(a)