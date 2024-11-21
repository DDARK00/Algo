n=int(input())

g = {"R":"S","P":"R","S":"P"}
cnt = n
wins = 0
s1 = input()
s2 = input()
for i in range(n):
    if s1[i] == s2[i]:
        cnt-=1
        continue
    wins+=g[s1[i]]==s2[i]
lose = cnt-wins
if wins>lose:
    print("victory")
else:
    print("defeat")