import sys
input = sys.stdin.readline

while True:
    origin = input().rstrip()
    if len(origin) == 0 :
        break
    origin = list(origin)
    answer_str = sorted(origin)
    answer_str = "".join(answer_str)
    answer_location = {}
    for idx, c in enumerate(answer_str):
        answer_location[c] = idx
        answer_location[idx] = c
    # 전처리
    
    cnt = 0
    for i in range(len(origin)):
        answer_str = answer_location[i]
        while origin[i] != answer_str:
            correct_idx = answer_location[origin[i]]
            cnt += 1
            origin[i], origin[correct_idx] = origin[correct_idx], origin[i]
            
            
    print(cnt)

    # 한번에 두 개 맞추는거 고려 안 했는데 될 것 같기도 하고 증명을 못하겠다.