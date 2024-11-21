while True:
    a,b= map(int, input().split())
    if not a and not b:break
    print(min(a, b) - max(a, b) + min(a, b))