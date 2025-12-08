from collections import deque

n, m = map(int, input().split())
q = deque()

visited = [False] * (100001)
q.append([n, 0])
visited[n] = True

dx = [-1, 1]

while q:
    x, count = q.popleft()

    if x == m:
        print(count)
        break

    nx = x * 2
    if 0 <= nx <= 100000 and not visited[nx]:
        q.appendleft([nx, count])
        visited[nx] = True
        
    for i in range(2):
        nx = x + dx[i]

        if 0 <= nx <= 100000 and not visited[nx]:
            q.append([nx, count + 1])
            visited[nx] = True