while True:
    try:
        s, t = input().split()
        #s가 t의 부분인가
        idx = 0
        for c in t:
            if idx<len(s) and c == s[idx]:
                idx+=1
        if idx == len(s):
            print("Yes")
        else:
            print("No")
        
    except Exception as e:
        # print("end")
        # print(e)
        break