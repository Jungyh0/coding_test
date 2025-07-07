import sys
input = sys.stdin.readline

num = []
str = []

for i in range(3):
    n = input()
    num.append(int(n))
    str.append(n.strip())
sum_str = str[0] + str[1]

print(num[0] + num[1] - num[2])
print(int(sum_str) - int(str[2]))