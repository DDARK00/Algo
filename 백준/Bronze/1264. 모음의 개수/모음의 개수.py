while True:
    s=input()
    if s=="#":
        break
    s=s.lower()
    print(sum(map(lambda x:s.count(x),"aeiou")))