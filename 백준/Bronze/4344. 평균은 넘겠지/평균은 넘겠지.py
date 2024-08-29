from functools import reduce

n = int(input())

for _ in range (n):
    one, *oth = map(int,input().split())
    list_len = len(oth)
    sums = reduce(lambda x,y:x+y,oth,0)
    
    avg = (sums/one)
    cnt = 0
    for i in oth:
        if i>avg :cnt+=1
        
    print(f'{cnt/one*100}%')