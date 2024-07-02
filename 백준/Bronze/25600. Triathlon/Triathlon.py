import sys
input = sys.stdin.readline

n = int(input())

m_score = 0
for _ in range(n):
    a, d, g = map(int, input().split())
    score = a*(d+g)
    if a == d+g:
        score *=2
    m_score = max(m_score, score)
print(m_score)