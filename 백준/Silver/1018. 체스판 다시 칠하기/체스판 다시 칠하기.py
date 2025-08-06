import sys

n, m = map(int, input().split())
board = []
cnt = []
for _ in range(n):
    sample = list(input().strip())
    board.append(sample)

for x in range(n - 7):
    for y in range(m - 7):
        w_count = 0
        b_count = 0
        for i in range(x, x + 8):
            for j in range(y, y + 8):
                if (i + j) % 2 == 0:
                    if board[i][j] == "W":
                        w_count += 1
                    else:
                        b_count += 1
                else:
                    if board[i][j] == "W":
                        b_count += 1
                    else:
                        w_count += 1
        cnt.append(w_count)
        cnt.append(b_count)
print(min(cnt))