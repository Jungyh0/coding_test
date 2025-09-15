import sys
input = sys.stdin.readline

n = int(input())
room = []
for _ in range(n):
    sample = list(map(int, input().split()))
    room.append(sample)

room = sorted(room, key = lambda x: (x[1], x[0]))

result = 1
end = room[0][1]
for i in range(1, n):
    if end <= room[i][0]:
        end = room[i][1]
        result += 1
print(result)