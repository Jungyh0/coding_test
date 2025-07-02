import sys
input = sys.stdin.readline

nn = [list(map(int, input().split()))for _ in range(9)]

max = nn[0][0]
x = 1
y = 1

for i in range(len(nn)):
    for j in range(len(nn[i])):
        if nn[i][j] > max:
            max = nn[i][j]
            x = i + 1
            y = j + 1
print(max)
print(x, y)
