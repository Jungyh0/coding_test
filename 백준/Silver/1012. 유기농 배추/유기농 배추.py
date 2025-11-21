import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = deque()

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    bug = 0

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    for i in range(m):
        for j in range(n):
            if graph[j][i] == 1:
                graph[j][i] = 0
                bug = bug + 1
                q. append([i, j])
                while q:
                    x, y = q.popleft()
                    for index in range(4):
                        nx = x + dx[index]
                        ny = y + dy[index]

                        if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:  
                            graph[ny][nx] = 0
                            q.append([nx, ny])
    print(bug)