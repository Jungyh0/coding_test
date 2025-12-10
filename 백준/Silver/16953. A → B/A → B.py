from collections import deque

n, m = map(int, input().split())

q = deque()
q.append([n, 1])
while q:
    x, count = q.popleft()
    if x == m:
        print(count)
        break
    elif x > m:
        continue
    for i in range(2):
        if i == 0:
            nx = 2 * x
            q.append([nx, count + 1])
        if i == 1:
            nx = int(str(x) + "1")
            q.append([nx, count + 1])
else:
  print(-1)