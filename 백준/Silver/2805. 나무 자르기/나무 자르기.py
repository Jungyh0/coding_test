import sys
input = sys.stdin.readline

n, m = map(int, input().split())

num = list(map(int, input().split()))

start = 1
end = max(num)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = 0

    for i in num:
        if i > mid:
            total += i - mid
    if total >= m:
        result = mid
        start = mid + 1
    elif total < m:
        end = mid - 1
print(result)