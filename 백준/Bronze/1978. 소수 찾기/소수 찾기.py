import sys
input = sys.stdin.readline

def check(input_num):
    check_num = 2
    if input_num < 2:
        return False
    while check_num <= input_num:
        if check_num != input_num and input_num % check_num == 0:
            return False
        check_num += 1
    return True

n = int(input())

num = list(map(int, input().split()))

answer = 0

for index in range(n):
    if check(num[index]):
        answer += 1
print(answer)