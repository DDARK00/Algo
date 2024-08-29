import sys
import math
from collections import defaultdict
input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    n, m = map(int,input().split())
    cars = {}
    for _ in range(n):
        name, *info = input().split()
        cars[name] = {
            "buy_cost" : int(info[0]),
            "rent_cost" : int(info[1]),
            "run_cost" : int(info[2])
        }
    temp = defaultdict(int)
    chk = defaultdict(str)
    ans = defaultdict(int)
    for _ in range(m):
        t, name, type, event = input().split()
        if ans[name] == "INCONSISTENT":
            continue
        if type == "r":
            if chk[name] != "" :
                ans[name] += temp[name] + cars[chk[name]]["run_cost"] * int(event)
                chk[name] = ""
                temp[name] = 0
            else:
                ans[name] = "INCONSISTENT"
        elif type == "a":
            if chk[name] != "":
                temp[name] += math.ceil(cars[chk[name]]["buy_cost"] * int(event) / 100)
            else:
                ans[name] = "INCONSISTENT"
        elif type == "p":
            if chk[name] == "":
                chk[name] = event
                temp[name] += cars[event]["rent_cost"]
            else:
                ans[name] = "INCONSISTENT"

    for key, value in temp.items():
        if value>0:
            ans[key] = "INCONSISTENT"

    answer = [(key,value) for key, value in ans.items()]
    answer.sort()
    for item in answer:
        print(item[0], item[1])
# 문제 진짜 이상해;;; 조건을 좀 줘라