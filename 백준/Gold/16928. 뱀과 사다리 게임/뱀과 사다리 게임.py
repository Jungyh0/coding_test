import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

ladder = {}
snake = {}
for _ in range(n):
    st, ed = map(int, input().split())
    ladder[st] = ed

for _ in range(m):
    st, ed = map(int, input().split())
    snake[st] = ed

board = [-1] * 101

q = deque([(1, 0)])
board[1] = 0

def bfs():
    while q:
        n_x, cnt = q.popleft()

        if n_x == 100:
            return cnt

        for dice_num in range(1, 7):
            next_x = n_x + dice_num

            if next_x > 100:
                continue

            final_x = next_x
            if next_x in ladder:
                final_x = ladder[next_x]
            elif next_x in snake:
                final_x = snake[next_x]
            
            if board[final_x] == -1 or board[final_x] > cnt + 1:
                board[final_x] = cnt + 1
                q.append((final_x, cnt + 1))
    
    return -1

print(bfs())
