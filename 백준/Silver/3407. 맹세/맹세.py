import sys
from collections import defaultdict, deque
input=sys.stdin.readline
atom=['h', 'b', 'c', 'n', 'o', 'f', 'p', 's', 'k', 'v', 'y', 'i', 'w', 'u', "ba", "ca" , "ga", "la", "na", "pa", "ra", "ta", "db", "nb", "pb", "rb", "sb", "tb", "yb", "ac", "sc", "tc", "cd", "gd", "md", "nd", "pd", "be", "ce", "fe", "ge", "he", "ne", "re", "se", "te", "xe", "cf", "hf", "rf", "ag", "hg", "mg", "rg", "sg", "bh", "rh", "th", "bi", "li", "ni", "si", "ti", "bk", "al", "cl", "fl", "tl", "am", "cm", "fm", "pm", "sm", "tm", "cn", "in", "mn", "rn", "sn", "zn", "co", "ho", "mo", "no", "po", "np", "ar", "br", "cr", "er", "fr", "ir", "kr", "lr", "pr", "sr", "zr", "as", "cs", "ds", "es", "hs", "os", "at", "mt", "pt", "au", "cu", "eu", "lu", "pu", "ru", "lv", "dy"]
dd=defaultdict(bool)
for at in atom:
    dd[at]=1

def solve():
    s=input().rstrip()
    q=deque([(0)]) # idx
    visited=[0]*50002
    while q:
        v=q.popleft()
        if v==len(s):
            return True

        if dd[s[v]]and not visited[v+1]:
            visited[v+1]=1
            q.append(v+1)

        if v+1<len(s) and dd[s[v]+s[v+1]] and not visited[v+2]:
            visited[v+2]=1
            q.append(v+2)
    return False

for _ in range(int(input())):
    if solve():
        print("YES")
    else:
        print("NO")