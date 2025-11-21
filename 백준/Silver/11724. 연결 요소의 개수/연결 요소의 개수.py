import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
q = deque()
num = 0

def bfs(start):
    q.append(start)

    while q:
        node = q.popleft()

        if len(graph[node]) > 0:
            for i in range(len(graph[node])):
                if not visited[graph[node][i]]:
                    visited[graph[node][i]] = True
                    q.append(graph[node][i])

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    if visited[i] == False:
        visited[i] = True
        bfs(i)
        num = num + 1

print(num)