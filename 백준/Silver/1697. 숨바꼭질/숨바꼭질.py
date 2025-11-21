import sys
input = sys.stdin.readline
from collections import deque

q = deque()
n, m = map(int, input().split())
visited = [False] * 100001

q.append([n, 0])
visited[n] = True
d = [1, -1]

while q:
    x, cnt = q.popleft()

    if x == m:
        print(cnt)
        break
    for i in range(3):
        if i < 2:
            nx = x + d[i]
        else:
            nx = x * 2
        if 0 <= nx <= 100000 and not visited[nx]:
            q.append([nx, cnt + 1])
            visited[nx] = True