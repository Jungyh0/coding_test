import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

dist1 = [-1] * (n + 1)
dist2 = [-1] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    v1, v2, weight = map(int, input().split())
    graph[v1].append((v2, weight))
    graph[v2].append((v1, weight))

def dfs(v, w, dist):
    for n_v, n_w in graph[v]:
        if dist[n_v] == -1:
            dist[n_v] = w + n_w
            dfs(n_v, dist[n_v], dist)
dist1[1] = 0          
dfs(1, 0, dist1)
idx = dist1.index(max(dist1))

dist2[idx] = 0 
dfs(idx, 0, dist2)
print(max(dist2))