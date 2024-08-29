import sys
input=sys.stdin.readline

case = 1
chk = {"1":["4","5"],
       "2":[],
       "3":["4","5"],
       "4":["2","3"],
       "5":["8"],
       "6":["2","3"],
       "7":["8"],
       "8":["6","7"],
      }
while True:
    r = input().rstrip()
    if r == "0":
        break
    v = "VALID"
    if r[0] != "1" or r[-1] != "2":
        v = "NOT"
    else:
        for i in range(len(r)-1):
            nxt = r[i+1]
            if nxt not in chk[r[i]]:
                v = "NOT"
                break

    print(f'{case}. {v}')
    case += 1