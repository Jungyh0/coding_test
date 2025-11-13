import sys
input = sys.stdin.readline
from collections import deque

n, m = map (int, input().split())
q = deque()
graph = [list (map (int, input().split())) for _ in range(n)]
result = [[-1] * m for _ in range(n)]

st_x = 0
st_y = 0
found = False
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            st_x = i
            st_y = j
            found = True
            break

        if found:
            break

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q.append([st_x, st_y, 0])
result[st_x][st_y] = 0

while q:
    x, y, cnt = q.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and result[nx][ny] == -1:
            result[nx][ny] = cnt + 1
            q.append([nx, ny, cnt + 1])

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and result[i][j] == -1:
            result[i][j] = 0

for line in result:
  print(*line)