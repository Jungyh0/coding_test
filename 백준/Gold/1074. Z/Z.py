import sys
import math

n, r, c = map(int, input().split())
ans = 0

while n != 0:
    n = n -1
    m = 2 ** n
    if r < m and c < m: 
        continue
    elif r < m and c >= m:
        ans = ans + (m * m)
        c = c - m
    elif r >= m and c < m:
        ans = ans + (m * m) * 2
        r = r - m
    else:
        ans = ans + (m * m) * 3
        r = r - m
        c = c - m
print(ans) 