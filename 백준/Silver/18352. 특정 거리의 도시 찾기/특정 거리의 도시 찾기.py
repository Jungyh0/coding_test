import sys
input = sys.stdin.readline
from collections import deque

n, m, k, x = map(int, input().split())

graph = [[]for _ in range(n + 1)]
visited = [False] * (n + 1)
dist = []

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)

visited[x] = True
q = deque([(x, 0)])

while q:
    v, d = q.popleft()

    if d == k:
        dist.append(v)
        continue
    for next_v in graph[v]:
        if not visited[next_v]:
            visited[next_v] = True
            q.append((next_v, d + 1))
if len(dist) > 0:
    dist.sort()
    for num in dist:
        print(num)
else:
    print(-1)