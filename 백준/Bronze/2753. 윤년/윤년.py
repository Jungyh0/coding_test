a = int(input())

n = a % 4
m = a % 100
x = a % 400

if n == 0:
    if m != 0:
        print(1)
    elif x == 0:
        print(1)
    else:
        print(0)
else:
    print(0)