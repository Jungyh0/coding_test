import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

visited = list(list(False for _ in range(n)) for _ in range(n))
graph = []

for i in range(1, n + 1):
    sample = list(map(int, input().split()))
    graph.append(sample)

q = deque([(0, 0)])
visited[0][0] = True
result = "Hing"
while q:
    x, y = q.popleft()

    val = graph[x][y]
    if val == -1:
        result = "HaruHaru"
        break
    nx = x + val
    ny = y + val

    if nx < n and not visited[nx][y]:
        visited[nx][y] = True
        q.append((nx, y))
    if ny < n and not visited[x][ny]:
        visited[x][ny] = True
        q.append((x, ny))

print(result)