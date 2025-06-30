a = [int(input()) for _ in range(9)]

max_v = 0
max_i = 0

for i in range (len(a)):
    if a[i] > max_v:
        max_v = a[i]
        max_i = i

print(max_v)
print(max_i + 1)