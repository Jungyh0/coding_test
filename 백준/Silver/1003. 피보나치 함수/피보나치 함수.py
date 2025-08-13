import sys
input = sys.stdin.readline

n = int(input())
count_zero = []
count_one = []

count_zero.insert(0, 1)
count_zero.insert(1, 0)

count_one.insert(0, 0)
count_one.insert(1, 1)


def Count_Zero(N):
    count_zero.insert(N, count_zero[N - 1] + count_zero[N - 2])

def Count_One(N):
    count_one.insert(N, count_one[N - 1] + count_one[N - 2])

for num in range(2, 41, 1):
    Count_Zero(num)
    Count_One(num)

for _ in range(n):
    m = int(input())
    print(count_zero[m], count_one[m])