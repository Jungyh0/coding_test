import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
q = deque(i + 1 for i in range(n))
search_num = list(map(int, input().split()))
cnt = 0

for i in search_num:
    while True:
        if q[0] == i:
            q.popleft()
            break
        else:
            if q.index(i) <= len(q) // 2:
                q.rotate(-1)
                cnt += 1
            else:
                q.rotate(1)
                cnt += 1

print(cnt)