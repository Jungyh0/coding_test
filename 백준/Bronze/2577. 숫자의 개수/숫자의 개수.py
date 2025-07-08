import sys
input = sys.stdin.readline

num_list = []
for _ in range(3):
    n = int(input())
    num_list.append(n)

n = num_list[0] * num_list[1] * num_list[2]
nn = list(map(int, str(n)))
for i in range(10):
    print(nn.count(i))