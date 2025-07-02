import sys
input = sys.stdin.readline
answer = 0
x = 0
y = 0
n = int(input())
nn = [[0] * 101 for _ in range(101)]

def draw(n_x, n_y):
    x_max = n_x + 10
    y_max = n_y + 10

    for i in range (n_x, x_max):
        for j in range (n_y, y_max):
            if nn[i][j] == 0:
                nn[i][j] = 1
            else:
                continue

for _ in range(n):
    x, y = map(int, input().split())
    draw(x, y)

for i in range(len(nn)):
    for j in range(len(nn[i])):
        if nn[i][j] == 1:
            answer += 1

print (answer)