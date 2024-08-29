n = int(input())

nums = list(map(int,input().split()))

maxlen = 1

now = 1

neu = 1

dir = ""

for i in range(1,len(nums)):

    bef = nums[i-1]

    if bef == nums[i]:

        neu += 1

        now+=1

        

        

        

    elif bef < nums[i]:

        if dir != "+":

            dir = "+"

            now = 1

            now+= neu

            neu = 1

            

        else:

            now+=1

            neu = 1

        

        

    elif bef > nums[i]:

        if dir != "-":

            dir = "-"

            now = 1

            now+= neu

            neu = 1

            

        else:

            now+=1

            neu = 1

            

    maxlen = max(maxlen,now)

print(maxlen)