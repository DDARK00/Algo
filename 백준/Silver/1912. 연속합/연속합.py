import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

max_s = nums[0]

temp = nums[0] if nums[0]>0 else 0
flag = True if nums[0] >0 else False
for i in range(1, n):
    num = nums[i]
    
    if flag and temp+nums[i] > 0:
        num += temp
        temp += nums[i]
        # 숫자가 연속으로 상승일 때
    
    elif nums[i]> 0:
        flag = True
        temp = nums[i]
        
    else:
        flag = False
        #들어온 수가 그냥 음수면
    max_s = max(max_s, num)
print(max_s)