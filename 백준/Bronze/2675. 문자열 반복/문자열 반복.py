import sys
input = sys.stdin.readline
n = int(input())

for _ in range(n):
    num, input_str = map(str, input().split())
    str_list = list(input_str.strip())
    asnwer = ""
    for i in range(len(str_list)):
        for _ in range(int(num)):
            asnwer += str_list[i]
    print(asnwer)