
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
visited = [False] * (n + 1)
dist_list = list([] for _ in range(n + 1))

for _ in range(n -1):
    v1, v2, dist = map(int, input().split())
    dist_list[v1].append((v2, dist))
    dist_list[v2].append((v1, dist))

q = deque([(1, 0)])
visited[1] = True
total = 0

while q:
    v, d = q.popleft()

    if d > total:
        total = d
    for next_v, next_d in dist_list[v]:
        if not visited[next_v]:
            q.append([next_v, d + next_d])
            visited[next_v] = True
print(total)
