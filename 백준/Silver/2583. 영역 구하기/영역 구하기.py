import sys
from collections import deque

input = sys.stdin.readline

m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

def bfs(y, x):
    q = deque([(y, x)])
    graph[y][x] = 1 
    count = 1
    
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= ny < m and 0 <= nx < n and graph[ny][nx] == 0:
                graph[ny][nx] = 1
                q.append((ny, nx))
                count += 1
    return count

result = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            result.append(bfs(i, j))

result.sort()
print(len(result))
print(*result)