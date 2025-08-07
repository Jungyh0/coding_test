import sys
input = sys.stdin.readline

n, m = map(int, input().split())

a = set()
b = set()

for _ in range(n):
    str = input().strip()
    a.add(str)
for _ in range(m):
    str = input().strip()
    b.add(str)

c = a.intersection(b)

print(len(c))
c = sorted(c)
for s in c:
    print(s)