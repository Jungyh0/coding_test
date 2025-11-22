import sys
input = sys.stdin.readline

n = int(input())
graph = []
w, b = 0, 0
for _ in range(n):
    sample = list(map(int, input().split()))
    graph.append(sample)

def checking(x, y, n):
    global w, b
    color = graph[y][x]

    for i in range(y, y + n):
        for j in range(x, x + n):
            if graph[i][j] != color:
                h = n // 2
                checking(x, y + h, h)
                checking(x + h, y, h)
                checking(x + h, y + h, h)
                checking(x, y, h)
                return
    if color == 0:
        w += 1
    else:
        b += 1

checking(0, 0, n)
print(w)
print(b)