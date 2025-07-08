n = int(input())

for _ in range(n):
    a = input()
    answer = 0
    num = 1
    for i in range(len(a)):
        if a[i] == 'O':
            answer += num
            num += 1
        else:
            num = 1
    print(answer)