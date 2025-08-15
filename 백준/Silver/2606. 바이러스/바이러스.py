import sys
input = sys.stdin.readline

result = 0
n = int(input())
m = int(input())
node =[[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    node1, node2 = map(int, input().split())
    node[node1].append(node2)
    node[node2].append(node1)

def dfs(st, graph):
    global result
    visited[st] = True
    for index in node[st]:
        if not visited[index]:
            result += 1
            dfs(index, graph)
dfs(1, node)

print(result)