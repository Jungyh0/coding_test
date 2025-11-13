import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

box = [list (map (int, input().split())) for _ in range(m)]

q = deque()

for x in range(m):
    for y in range(n):
        if box[x][y] == 1:
            q.append([x, y])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans = 0

while q:
    x, y = q.popleft()
    l = len(q)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            if box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                q.append([nx, ny])
    
for line in box:
    for tomato in line:
        if tomato == 0:
            print(-1)
            exit()
    ans = max(ans, max(line))

print(ans - 1)