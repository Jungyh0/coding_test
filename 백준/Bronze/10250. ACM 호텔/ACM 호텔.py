import sys
input = sys.stdin.readline
r = int(input())

for _ in range(r):
    h, w, n = map(int, input().split())

    hun = 1
    o = 1

    for i in range(n - 1):
        if hun != h:
            hun += 1
        else:
            hun = 1
            o += 1

    print(hun * 100 + o)