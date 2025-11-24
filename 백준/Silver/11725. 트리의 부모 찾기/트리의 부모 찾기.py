import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
ans = [0] * (n + 1)

for _ in range(n - 1):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def bfs():
    q = deque()
    q.append(1) 
    visited[1] = True

    while q:
        now = q.popleft()

        for next_node in graph[now]:
            if not visited[next_node]:
                visited[next_node] = True
                ans[next_node] = now 
                q.append(next_node)

bfs()

for i in range(2, n + 1):
    print(ans[i])