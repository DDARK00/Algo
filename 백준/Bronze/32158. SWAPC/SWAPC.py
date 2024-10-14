import sys
input = sys.stdin.readline
n = int(input())
s = input().rstrip()
target_cnt = s.count("P")
target_cnt = min(s.count("C"), target_cnt)

s = s.replace("P","*",target_cnt)
s = s.replace("C","P",target_cnt)
s = s.replace("*","C")
print(s)