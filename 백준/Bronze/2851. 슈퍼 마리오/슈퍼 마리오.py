ans = 0

for n in [int(input()) for _ in range(10)]:
    if abs(100-ans-n)<=abs(100-ans):
        ans+=n
    else:
        break
print(ans)