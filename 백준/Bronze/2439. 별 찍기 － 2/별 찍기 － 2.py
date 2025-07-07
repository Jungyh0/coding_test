import sys
input = sys.stdin.readline

n = int(input())
for i in range(n - 1, -1, -1):
    star_num = n - i
    space_num = n - star_num
    space_str = " " * space_num
    star_str = space_str + ("*" * star_num)
    print(star_str)