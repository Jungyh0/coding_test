import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

arr2 = sorted(list(set(arr)))

dic = {arr2[i] : i for i in range(len(arr2))}

for i in range(n):
    arr[i] = dic[arr[i]]

print(*arr)